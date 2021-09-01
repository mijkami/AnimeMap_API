# About
FastAPI implementation for the [anime_map project](https://github.com/mijkami/anime_map) that will be used to serve information to the front-end, using the .joblib model resulting from the aforementioned project.

# Installation
- clone projet
- create **/data** folder at the root
- add in /data the following files:

  - anime_df_relevant_PG.csv
  - active_users_df_10PlusRatings_partial.csv
  - models_anime_map_knn_model.joblib

# Run the server
## Run locally
- > make run_api
- access http://127.0.0.1:8080

## Run on Docker
### (linux) enable and start docker
- sudo systemctl enable docker
- sudo systemctl start docker

### create docker image
- sudo docker build -t anime_map_api .   

### run the server
- sudo docker run -it -e PORT=8080 -p 8080:8080 anime_map_api


# How to use it

- pick an anime name from [MyAnimeList](https://myanimelist.net/topanime.php) (for example 'Naruto')
- ask the API at the address it is installed, for example on localhost asking for 'Naruto': ```http://127.0.0.1:8080/predict?anime=Naruto```
- if you want a specific length, add a length argument like this: ```http://127.0.0.1:8080/predict?anime=Bleach&length=40```
- use the given .json for your frontend purposes