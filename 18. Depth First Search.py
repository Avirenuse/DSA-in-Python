# Depth First Search (DFS) Algorithm for Graphs
# A traversal algorithm that starts at the root (or selected node) and explores as far as possible 
# along each branch before backtracking.
# Time Complexity: O(V + E) where V is vertices and E is edges
# Space Complexity: O(V)

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
        
    def dfs_util(self, vertex, visited, result):
        # Mark the current node as visited and store it
        visited.add(vertex)
        result.append(vertex)
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)
                
    def dfs(self, start_vertex):
        # Set to store visited vertices
        visited = set()
        result = []
        
        # Call the recursive helper function to print DFS traversal
        # starting from the given vertex
        self.dfs_util(start_vertex, visited, result)
        
        return result
        
    def dfs_all(self):
        # Handles disconnected graphs by calling DFS for all vertices
        visited = set()
        result = []
        
        for vertex in self.graph:
            if vertex not in visited:
                self.dfs_util(vertex, visited, result)
                
        return result

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Following is Depth First Traversal (starting from vertex 2):")
    dfs_result = g.dfs(2)
    print(" -> ".join(map(str, dfs_result)))
