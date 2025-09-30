# main.py
from graph import Graph, find_shortest_path
from datetime import datetime
from collections import deque

FARE_PER_UNIT_DISTANCE = 10  # 10 units per distance
SURGE_MULTIPLIER = 1.5       # applied if demand > supply

def log_trip(driver, pickup, destination, path, cost, total_fare, rating):
    """Append trip details to trips.log file."""
    with open("trips.log", "a") as f:
        f.write(
            f"[{datetime.now()}] Driver: {driver}, Pickup: {pickup}, "
            f"Destination: {destination}, Route: {path}, Cost: {cost}, "
            f"Fare: {total_fare}, Rating: {rating}\n"
        )

class Dispatcher:
    def __init__(self, city, drivers):
        self.city = city
        self.available_drivers = drivers.copy()  # {driver: location}
        self.driver_ratings = {driver: [] for driver in drivers}  # list of ratings
        self.rider_queue = deque()  # waiting riders (pickup, destination)

    def request_ride(self, pickup, destination):
        print(f"\n📢 Rider requests trip from {pickup} to {destination}")
        if not self.available_drivers:
            print("⚠️ No drivers available, adding rider to waiting queue...")
            self.rider_queue.append((pickup, destination))
        else:
            self.assign_driver(pickup, destination)

    def assign_driver(self, pickup, destination):
        # Surge pricing check
        if len(self.rider_queue) > len(self.available_drivers):
            surge_multiplier = SURGE_MULTIPLIER
            print("⚡ Surge pricing applied!")
        else:
            surge_multiplier = 1

        # Find nearest driver
        nearest_driver = None
        nearest_path = None
        min_cost = float("inf")

        for driver, loc in self.available_drivers.items():
            path, cost = find_shortest_path(self.city, loc, pickup)
            if path and cost < min_cost:
                nearest_driver = driver
                nearest_path = path
                min_cost = cost

        if nearest_driver:
            pickup_distance = min_cost
            print(f"✅ Assigned {nearest_driver} to rider at {pickup}")
            print(f"   Pickup route: {nearest_path}, Distance: {pickup_distance}")

            # Trip from pickup to destination
            trip_path, trip_distance = find_shortest_path(self.city, pickup, destination)
            total_distance = pickup_distance + trip_distance
            total_fare = total_distance * FARE_PER_UNIT_DISTANCE * surge_multiplier

            print(f"🛣️ Trip route: {trip_path}, Distance: {trip_distance}")
            print(f"💰 Total fare (pickup + trip, surge applied if any): {total_fare:.2f} units")
            print(f"🎉 {nearest_driver} completed the trip!")

            # Ask for rating
            while True:
                try:
                    rating = float(input(f"⭐ Rate {nearest_driver} (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("⚠️ Enter a value between 1 and 5")
                except ValueError:
                    print("⚠️ Enter a number")
            self.driver_ratings[nearest_driver].append(rating)
            avg_rating = sum(self.driver_ratings[nearest_driver]) / len(self.driver_ratings[nearest_driver])
            print(f"📊 {nearest_driver}'s average rating: {avg_rating:.2f}")

            # Log trip
            log_trip(nearest_driver, pickup, destination, trip_path, trip_distance, total_fare, rating)

            # Update driver's location
            self.available_drivers[nearest_driver] = destination

            # Check waiting riders
            if self.rider_queue:
                next_pickup, next_dest = self.rider_queue.popleft()
                print(f"\n🚦 Dispatching waiting rider from {next_pickup} to {next_dest}...")
                self.assign_driver(next_pickup, next_dest)

def main():
    # Build city map
    city = Graph()
    city.add_edge("A", "B", 5)
    city.add_edge("A", "C", 10)
    city.add_edge("B", "D", 2)
    city.add_edge("C", "D", 3)
    city.add_edge("B", "E", 7)
    city.add_edge("D", "E", 1)

    print("🚕 Mini Uber Simulation with Surge & Ratings 🚕")

    # Drivers
    drivers = {
        "Driver1": "C",
        "Driver2": "B",
    }
    dispatcher = Dispatcher(city, drivers)

    # Interactive CLI loop
    while True:
        print("\n--- New Ride Request ---")
        pickup = input("Enter pickup location (or 'exit' to quit): ")
        if pickup.lower() == "exit":
            print("Exiting simulation. Goodbye!")
            break
        destination = input("Enter destination: ")
        dispatcher.request_ride(pickup, destination)

if __name__ == "__main__":
    main()

