from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.core.simulation import run_simulation


app = FastAPI(title="Mini Uber API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for POST request body
class RideRequest(BaseModel):
    pickup: str
    destination: str


@app.get("/")
def home():
    return {"message": "🚕 Mini Uber API is running"}


@app.get("/ride")
def request_ride(pickup: str, destination: str):
    result = run_simulation(pickup, destination)
    return result


@app.post("/simulate")
def simulate_ride(request: RideRequest):
    result = run_simulation(request.pickup, request.destination)
    return {
        "status": "confirmed",
        "pickup": request.pickup,
        "destination": request.destination,
        "simulation": result
    }

