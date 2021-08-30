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
def predict_animes(predict_input):
    params = {
            "predict_input": [predict_input]
                }
    y_pred = predict.recommendation_10PlusRatings(f'{predict_input}')
    return {"features": params,
            "prediction": y_pred
            }        
