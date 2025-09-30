from core.simulation import run_simulation

def main():
    print("🚕 Mini Uber Simulation 🚕\n")

    pickup, destination = "A", "E"
    print(f"📢 Rider requests trip from {pickup} to {destination}")

    result = run_simulation(pickup, destination)

    if "error" in result:
        print("❌", result["error"])
    else:
        print(f"✅ Assigned {result['assigned_driver']} to rider at {pickup}")
        print(f"   Pickup route: {result['pickup_route']}")
        print(f"   Trip route: {result['trip_route']}")
        print(f"   Total distance: {result['distance']}")
        print(f"   Fare: {result['fare']}")

if __name__ == "__main__":
    main()

