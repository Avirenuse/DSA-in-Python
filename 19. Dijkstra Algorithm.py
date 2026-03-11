# Dijkstra's Shortest Path Algorithm
# An algorithm for finding the shortest paths between nodes in a graph.
# Time Complexity: O((V + E) log V) with a priority queue
# Space Complexity: O(V)

import heapq

class Graph:
    def __init__(self):
        # Represent graph using an adjacency list with weights
        # {vertex: [(weight, neighbor), ...]}
        self.graph = {}
        
    def add_edge(self, u, v, weight):
        # Undirected graph edge
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))
        
    def dijkstra(self, start_vertex):
        # Dictionary to store the shortest distances from start_vertex
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        
        # Priority queue to store vertices that are being pre-processed.
        # It stores tuples of (distance, vertex)
        pq = [(0, start_vertex)]
        
        # Dictionary to store the shortest path tree
        # Helps reconstruct the path later
        shortest_path_tree = {}
        
        while pq:
            # The first vertex in priority queue is the minimum distance vertex
            current_distance, current_vertex = heapq.heappop(pq)
            
            # Nodes can get added to the priority queue multiple times.
            # We only process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue
                
            # Explore neighbors
            for weight, neighbor in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_path_tree[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
                    
        return distances, shortest_path_tree

def print_path(shortest_path_tree, start_vertex, end_vertex):
    path = []
    current_vertex = end_vertex
    
    while current_vertex != start_vertex:
        if current_vertex not in shortest_path_tree:
            return "No path exists"
        path.append(current_vertex)
        current_vertex = shortest_path_tree[current_vertex]
        
    path.append(start_vertex)
    path.reverse()
    return " -> ".join(map(str, path))

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    
    start_node = 0
    distances, path_tree = g.dijkstra(start_node)
    
    print(f"Shortest distances from node {start_node}:")
    for vertex, distance in distances.items():
        print(f"To node {vertex}: {distance}")
        
    print(f"\nShortest path from 0 to 4:")
    print(print_path(path_tree, 0, 4))
