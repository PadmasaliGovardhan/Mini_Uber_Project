from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.simulation import run_simulation

app = FastAPI(title="Mini Uber API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ridewithus-92bdvu14d-padmasaligovardhans-projects.vercel.app",  
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "🚕 Mini Uber API is running"}

@app.get("/ride")
def request_ride(pickup: str, destination: str):
    result = run_simulation(pickup, destination)
    return result

