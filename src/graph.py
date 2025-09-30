# src/graph.py
import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight=1.0):
        if weight < 0:
            raise ValueError("Weight must be non-negative")
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def neighbors(self, node):
        return self.adj.get(node, [])

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.adj}
    prev = {node: None for node in graph.adj}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph.neighbors(u):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))
    return dist, prev

def reconstruct_path(prev, start, end):
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev.get(cur)
    path.reverse()
    if path and path[0] == start:
        return path
    return []
# graph.py (make sure this is your function)
def find_shortest_path(graph, start, end):
    import heapq

    pq = [(0, start, [])]  # (cost, current_node, path_so_far)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == end:
            return path, cost   # ✅ always returns tuple (list, int)

        for neighbor, weight in graph.neighbors(node):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return None, float("inf")  # if no path exists

