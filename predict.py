import joblib
import pandas as pd
from sklearn.neighbors import NearestNeighbors

model_path = "data/models_anime_map_knn_model.joblib"
model = joblib.load(model_path)

def get_anime():
    anime_df_relevant_PG = pd.read_csv("data/anime_df_relevant_PG.csv")
    return anime_df_relevant_PG.rename(columns={'MAL_ID' : 'anime_id'})

def get_data(name_file):
    data = pd.read_csv(f'data/{name_file}.csv')
    return data

def get_model(path):
    return joblib.load(model_path)

def process_data(name_file):
    data_users_df = get_data(name_file)
    data_users_df['rating'] = data_users_df['rating']/10
    
    anime_df_relevant_PG = get_anime()
    anime_name_df = anime_df_relevant_PG[['anime_id','Name']]
    data_users_df_merge = data_users_df.merge(anime_name_df, on = 'anime_id', how='inner')
    pivot_df = data_users_df_merge.pivot_table(index='anime_id',columns='user_id',values='rating').fillna(0)
    
    anime_Genres_df = anime_df_relevant_PG[['anime_id','Genres']]
    anime_Genres_df_encoded = pd.concat(objs = [anime_Genres_df.drop(columns = 'Genres', axis =1), anime_Genres_df['Genres'].str.get_dummies(sep=", ")], axis = 1)
    anime_Genres_df_encoded = anime_Genres_df_encoded.set_index('anime_id')
    
    pivot_df = pivot_df.merge(anime_Genres_df_encoded, how='inner',left_index=True, right_index=True)
    anime_name_pivot_df = data_users_df_merge[['anime_id','Name']].drop_duplicates()
    anime_name_pivot_df = anime_name_pivot_df.sort_values('anime_id')
    anime_name_pivot_df = anime_name_pivot_df.reset_index().drop(columns = 'index')
    
    return pivot_df, anime_name_pivot_df

def recommendation_10PlusRatings(anime_name, nb_recomendation = 10):
    pivot_df, anime_name_pivot_df = process_data('active_users_df_10PlusRatings_partial')
    model = get_model(model_path)
    index_nb = anime_name_pivot_df.index[anime_name_pivot_df['Name'] == anime_name].tolist()[0]
    distances, indices = model.kneighbors(pivot_df.iloc[index_nb,:].values.reshape(1, -1), n_neighbors = nb_recomendation + 1)

    prediction = []
    for i in range(0, len(distances.flatten())):
        if i == 0:
            prediction.append([pivot_df.index[indices.flatten()[i]],0])
        else:
            prediction.append([pivot_df.index[indices.flatten()[i]],distances.flatten()[i]])
    results = []
    for i in range(len(prediction)):
        anime_name = anime_name_pivot_df.query(f'anime_id == {prediction[i][0]}').iloc[0].Name
        distance = prediction[i][1]
        results.append([anime_name,distance])
    return results








