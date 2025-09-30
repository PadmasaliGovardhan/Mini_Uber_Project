from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.simulation import run_simulation

app = FastAPI(title="Mini Uber API")

# ✅ Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to ["http://127.0.0.1:5500"] later
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

