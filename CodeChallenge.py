from typing import List

class Building:
    def __init__(self, name: str, distance: dict):
        self.name = name
        self.distance = distance

def delivery_route_optimization(buildings: List[Building], start: Building) -> List[Building]:
    # Create a graph of the buildings
    graph = {}
    for building in buildings:
        graph[building.name] = building.distance

    # Apply the nearest-neighbor algorithm to find the shortest route
    visited = set([start.name])
    current = start.name
    route = [start]
    while len(visited) < len(graph):
        next_vertex = None
        next_distance = float('inf')
        for neighbor in graph[current]:
            if neighbor not in visited:
                distance = graph[current][neighbor]
                if distance < next_distance:
                    next_vertex = neighbor
                    next_distance = distance
        visited.add(next_vertex)
        next_building = next(b for b in buildings if b.name == next_vertex)
        route.append(next_building)
        current = next_vertex
    route.append(start)
    return route
