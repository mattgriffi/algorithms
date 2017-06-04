"""This program solves the classic word ladder problem using a Graph."""


from data_structures.graph import Graph


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
