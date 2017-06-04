"""This class implements a Graph."""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return f"{self.id} connected to: {[vertex.id for vertex in self.connected_to]}"
