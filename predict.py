import joblib
import pandas as pd
from sklearn.neighbors import NearestNeighbors


NOTATION_MODEL_PATH = "data/anime_map_data_animelist_100plus_PG_knn_model.joblib"
NOTATION_PIVOT_DF_NAME = "anime_map_data_animelist_100plus_PG_PCA_vector_df"
NOTATION_ANIME_NAME_PIVOT_NAME = "anime_map_data_animelist_100plus_PG_anime_name_pivot_df"

RATING_COMPLETED_MODEL_PATH = "data/anime_map_data_rating_complete_100plus_PG_knn_model.joblib"
RATING_COMPLETED_PIVOT_DF_NAME = "anime_map_data_rating_complete_100plus_PG_PCA_vector_df"
RATING_COMPLETED_ANIME_NAME_PIVOT_NAME = "anime_map_data_rating_complete_100plus_PG_anime_name_pivot_df"


def get_data(name_file):
    data = pd.read_csv(f'data/{name_file}.csv')
    return data

def get_model(path):
    return joblib.load(path)

def recommendation_10PlusRatings(anime_name, nb_recomendation, model):
    if model == 'notation':
        pivot_df = get_data(NOTATION_PIVOT_DF_NAME)
        anime_name_pivot_df = get_data(NOTATION_ANIME_NAME_PIVOT_NAME)
        model = get_model(NOTATION_MODEL_PATH)
    elif model == 'completed':
        pivot_df = get_data(RATING_COMPLETED_PIVOT_DF_NAME)
        anime_name_pivot_df = get_data(RATING_COMPLETED_ANIME_NAME_PIVOT_NAME)
        model = get_model(RATING_COMPLETED_MODEL_PATH)

    index_nb = anime_name_pivot_df.index[anime_name_pivot_df['Name'] == anime_name].tolist()[0]
    distances, indices = model.kneighbors(pivot_df.iloc[index_nb,:].values.reshape(1, -1), n_neighbors = nb_recomendation + 1)
    
    prediction = []
    for i in range(0, len(distances.flatten())):
        prediction.append([pivot_df.index[indices.flatten()[i]],distances.flatten()[i]])
    results = {}
    for i in range(len(prediction)):
        anime_name = anime_name_pivot_df.iloc[prediction[i][0]].Name
        distance = prediction[i][1]
        results[f'{anime_name}'] = distance
    return results













