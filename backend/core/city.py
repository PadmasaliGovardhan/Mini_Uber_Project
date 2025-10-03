from .graph import Graph
from .driver import Driver

def create_sample_city():
    graph = Graph()
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 10)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "E", 4)

    drivers = [
        Driver("Driver1", "C"),
        Driver("Driver2", "B"),
        Driver("Driver3", "E"),
    ]
    return graph, drivers

