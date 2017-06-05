"""This class implements a Graph."""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Adds a new vertex with id key to the graph, and returns the new Vertex object."""
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        """Returns vertex with id key if it exists the graph, else returns None."""
        return self.vertices.get(key, None)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Adds an edge between two vertices. Will create the vertices if they do not already
        exist in the graph."""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].add_neighbor(self.vertices[to_vertex], weight)

    def get_vertices(self):
        """Returns a list of vertex ids in this graph. To access the vertex objects instead,
        use __iter__"""
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, key):
        return key in self.vertices


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = "white"
        self.distance = 0
        self.predecessor = None
        self.discovery_time

    def add_neighbor(self, neighbor, weight=0):
        """Creates a new edge from this vertex to the neighbor."""
        self.connected_to[neighbor] = weight

    def get_connections(self):
        """Returns a list of the vertex objects that this vertex is connected to."""
        return list(self.connected_to.keys())

    def get_weight(self, neighbor):
        """Returns the weight of the edge from this vertex to neighbor"""
        return self.connected_to[neighbor]

    def __str__(self):
        return f"{self.id} connected to: {[vertex.id for vertex in self.connected_to]}"
