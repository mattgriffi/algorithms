"""This class extends Graph to make it easier to implement DFS."""


from data_structures.graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def depth_first_search(self):
        """Performs a depth first search on the graph, creating a depth first forest."""
        # Reset all vertices to white
        for vertex in self:
            vertex.color = "white"
            vertex.predecessor = None
        # Recursively search through the vertices
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        """Recursively performs a depth first search through the graph."""
        # Set the current vertex to gray
        start_vertex.color = "gray"
        self.time += 1
        start_vertex.discovery_time = self.time
        # Iterate through all neighboring vertices
        for next_vertex in start_vertex.get_connections():
            # If they haven't been visited yet
            if next_vertex.color == "white":
                next_vertex.predecessor = start_vertex
                # Recursively move to them
                self.dfs_visit(next_vertex)
        # After all neighboring vertices have been visited, mark vertex as black
        start_vertex.color = "black"
        self.time += 1
        start_vertex.finish_time = self.time