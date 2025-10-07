# backend/core/simulation.py

import random

# Define city connections and distances (in km)
city_graph = {
    "Vijayawada": {"Mangalagiri": 15, "Tadepalli": 10},
    "Mangalagiri": {"Vijayawada": 15, "Vaddeswaram": 8},
    "Vaddeswaram": {"Mangalagiri": 8, "Tadepalli": 5},
    "Tadepalli": {"Vaddeswaram": 5, "Machilipatnam": 70},
    "Machilipatnam": {"Tadepalli": 70, "Chirala": 80},
    "Chirala": {"Machilipatnam": 80, "Bapatla": 20},
    "Bapatla": {"Chirala": 20},
}

drivers = [
    {"name": "Driver1", "vehicle": "Sedan", "rating": 4.7},
    {"name": "Driver2", "vehicle": "Hatchback", "rating": 4.5},
    {"name": "Driver3", "vehicle": "SUV", "rating": 4.9},
]

# Simple Dijkstra for route finding
def find_shortest_route(graph, start, end):
    import heapq
    distances = {city: float("inf") for city in graph}
    distances[start] = 0
    queue = [(0, start, [start])]

    while queue:
        dist, node, path = heapq.heappop(queue)
        if node == end:
            return path, dist
        for neighbor, cost in graph[node].items():
            new_dist = dist + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor, path + [neighbor]))

    return None, float("inf")


def run_simulation(pickup, destination):
    if pickup not in city_graph or destination not in city_graph:
        return {"error": "Invalid city name"}
    if pickup == destination:
        return {"error": "Pickup and destination must be different"}

    path, distance = find_shortest_route(city_graph, pickup, destination)

    if not path or distance == float("inf"):
        return {"error": "No route found"}

    driver = random.choice(drivers)
    fare = round(distance * 10, 2)  # ₹10/km
    time_hr = round(distance / 40, 2)  # 40 km/h average

    return {
        "status": "confirmed",
        "driver_assigned": driver,
        "trip_route": path,
        "distance_km": distance,
        "estimated_time_hr": time_hr,
        "estimated_fare_inr": fare,
    }

