"""This program solves the classic word ladder problem using a Graph."""


from data_structures.graph import Graph
from data_structures.queue import Queue


def build_graph(word_file):
    buckets = {}
    graph = Graph()

    with open(word_file) as f:
        for line in f:
            word = line.strip()
            # Create buckets where each bucket is a word with 1 wildcard in it. Sort the words
            # into the buckets. Every word in a bucket will differ by 1 letter
            for i in range(len(word)):
                bucket = f"{word[:i]}_{word[i+1:]}"  # Example: POPE -> PO_E
                if bucket in buckets:
                    buckets[bucket].append(word)
                else:
                    buckets[bucket] = [word]
    # Create a vertex for every word, and add edges between words in the same bucket
    for bucket in buckets.values():
        for word1 in bucket:
            for word2 in bucket:
                if word1 != word2:
                    graph.add_edge(word1, word2)

    return graph


def breadth_first_search(graph, start):

    start.distance = 0
    start.predecessor = None
    vertex_queue = Queue()
    vertex_queue.enqueue(start)

    while not vertex_queue.isEmpty():
        current_vertex = vertex_queue.dequeue()

        for neighbor in current_vertex.get_connections():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current_vertex.distance + 1
                neighbor.predecessor = current_vertex
                vertex_queue.enqueue(neighbor)
        current_vertex.color = "black"


def traverse_bfs_tree(start):
    current_vertex = start
    while current_vertex.predecessor is not None:
        print(current_vertex.id)
        current_vertex = current_vertex.predecessor
    print(current_vertex.id)


graph = build_graph("words.txt")

breadth_first_search(graph, graph.get_vertex("fool"))

traverse_bfs_tree(graph.get_vertex("sage"))