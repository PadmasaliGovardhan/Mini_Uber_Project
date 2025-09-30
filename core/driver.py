class Driver:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return f"Driver({self.name} at {self.location})"

