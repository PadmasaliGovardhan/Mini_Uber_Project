from core.city import create_sample_city
from core.dispatcher import Dispatcher

def run_simulation(pickup, destination):
    graph, drivers = create_sample_city()
    dispatcher = Dispatcher(graph, drivers)

    result = dispatcher.assign_driver(pickup, destination)

    if result:
        return {
            "assigned_driver": result["driver"].name,
            "pickup_route": result["pickup_path"],
            "trip_route": result["trip_path"],
            "distance": result["distance"],
            "fare": result["fare"]
        }
    else:
        return {"error": "No available driver"}

