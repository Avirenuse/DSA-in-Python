#A Graph is a non-linear data structure that consists of vertices (nodes) and edges

'''A vertex, also called a node, is a point or an object in the Graph, and an edge is used to connect two vertices with each other.

Graphs are non-linear because the data structure allows us to have different paths to get from one vertex to another, unlike with linear data structures like Arrays or Linked Lists.

Graphs are used to represent and solve problems where the data consists of objects and relationships between them, such as:

Social Networks: Each person is a vertex, and relationships (like friendships) are the edges. Algorithms can suggest potential friends.
Maps and Navigation: Locations, like a town or bus stops, are stored as vertices, and roads are stored as edges. Algorithms can find the shortest route between two locations when stored as a Graph.
Internet: Can be represented as a Graph, with web pages as vertices and hyperlinks as edges.
Biology: Graphs can model systems like neural networks or the spread of diseases.
'''

"""Graph Representations
A Graph representation tells us how a Graph is stored in memory.

Different Graph representations can:

take up more or less space.
be faster or slower to search or manipulate.
be better suited depending on what type of Graph we have (weighted, directed, etc.), and what we want to do with the Graph.
be easier to understand and implement than others.
Below are short introductions of the different Graph representations, but Adjacency Matrix is the representation we will use for Graphs moving forward in this tutorial, as it is easy to understand and implement, and works in all cases relevant for this tutorial.

Graph representations store information about which vertices are adjacent, and how the edges between the vertices are. Graph representations are slightly different if the edges are directed or weighted.

Two vertices are adjacent, or neighbors, if there is an edge between them.

Adjacency Matrix Graph Representation
Adjacency Matrix is the Graph representation (structure) we will use for this tutorial.

How to implement an Adjacency Matrix is shown on the next page.

The Adjacency Matrix is a 2D array (matrix) where each cell on index (i,j) stores information about the edge from vertex i to vertex j."""


