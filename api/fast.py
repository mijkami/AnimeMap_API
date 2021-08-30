from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
def index():
    return {
        "greeting": "Hello world"
        }


@app.get("/predict")
def predict_animes(anime, length:int = 20):
    y_pred = predict.recommendation_10PlusRatings(anime, length)
    return {"predict_input": anime,
            "prediction": y_pred
            }        
