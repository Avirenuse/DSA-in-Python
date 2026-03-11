# Breadth First Search (BFS) Algorithm for Graphs
# A traversal algorithm where you start traversing from a selected node (source or starting node) 
# and traverse the graph layerwise thus exploring the neighbour nodes based on layer.
# Time Complexity: O(V + E) where V is vertices and E is edges
# Space Complexity: O(V)

from collections import deque

class Graph:
    def __init__(self):
        # Represent graph using an adjacency list
        self.graph = {}
        
    def add_edge(self, u, v):
        # Directed graph edge u -> v
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
            
        self.graph[u].append(v)
        
    def bfs(self, start_vertex):
        # Track visited vertices
        visited = set()
        
        # Create a queue for BFS
        queue = deque()
        
        # Mark the source node as visited and enqueue it
        visited.add(start_vertex)
        queue.append(start_vertex)
        
        result = []
        
        while queue:
            # Dequeue a vertex from queue and add it to result
            vertex = queue.popleft()
            result.append(vertex)
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return result

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Following is Breadth First Traversal (starting from vertex 2):")
    bfs_result = g.bfs(2)
    print(" -> ".join(map(str, bfs_result)))
