from core.graph import find_shortest_path

FARE_PER_UNIT_DISTANCE = 10  # adjustable

class Dispatcher:
    def __init__(self, graph, drivers):
        self.graph = graph
        self.drivers = drivers

    def assign_driver(self, pickup, destination):
        best_driver = None
        min_distance = float("inf")
        best_pickup_path = []
        best_trip_path = []

        for driver in self.drivers:
            pickup_path, pickup_distance = find_shortest_path(self.graph, driver.location, pickup)
            trip_path, trip_distance = find_shortest_path(self.graph, pickup, destination)

            if pickup_distance + trip_distance < min_distance:
                min_distance = pickup_distance + trip_distance
                best_driver = driver
                best_pickup_path = pickup_path
                best_trip_path = trip_path

        if not best_driver:
            return None

        total_fare = min_distance * FARE_PER_UNIT_DISTANCE
        best_driver.location = destination  # driver moves

        return {
            "driver": best_driver,
            "pickup_path": best_pickup_path,
            "trip_path": best_trip_path,
            "distance": min_distance,
            "fare": total_fare
        }

