"""This program solves the Knight's Tour chess puzzle with a depth first search on a Graph."""

import time

from data_structures.graph import Graph


def main():
    board_size = 8
    starting_square = 0
    board = knight_graph(board_size)
    knight_path = []
    start = time.time()
    knight_tour(0, knight_path, board.get_vertex(starting_square), 63)
    print(f"Our brave knight took {time.time()-start:.10f} seconds to complete his journey.")
    print([vertex.id for vertex in knight_path])


def knight_graph(board_size):
    """Generates a graph representing all possible moves of a knight on a chess board of given
    width."""
    graph = Graph()

    for row in range(board_size):
        for col in range(board_size):
            current_node_id = position_to_node_id(row, col, board_size)
            legal_move_positions = generate_legal_moves(row, col, board_size)
            for position in legal_move_positions:
                legal_move_node_id = position_to_node_id(*position, board_size)
                graph.add_edge(current_node_id, legal_move_node_id)

    return graph


def position_to_node_id(row, column, board_size):
    """Converts a row-column address to an integer id for a graph vertex."""
    return (row * board_size) + column


def generate_legal_moves(x, y, board_size):
    """Returns a list of tuples representing the (x, y) coordinates of all legal moves for
    a knight from the given (x, y) coordinate."""
    legal_moves = []
    move_offsets = [
        (-1, -2), (-1, 2), (-2, -1), (-2, 1),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    for offset in move_offsets:
        move_coord = (x + offset[0], y + offset[1])
        if legal_coord(*move_coord, board_size):
            legal_moves.append(move_coord)
    return legal_moves


def legal_coord(x, y, board_size):
    """Returns True if the given coordinate is on the board, else False."""
    return 0 <= x < board_size and 0 <= y < board_size


def knight_tour(current_depth, path, current_vertex, limit):
    """Uses depth first search to find the path a knight can take from a given starting node
    such that it visits every square on a chess board."""
    # Mark the vertex gray to show we've already been here
    current_vertex.color = "gray"
    path.append(current_vertex)
    # If we haven't already visited the required number of vertices
    if current_depth < limit:
        # Get all the neighbors of the current vertex
        neighbor_list = current_vertex.get_connections()
        done = False
        for neighbor in neighbor_list:
            # If a neighbor is unvisited (white)
            if neighbor.color == "white":
                # Recursively search from that vertex
                done = knight_tour(current_depth + 1, path, neighbor, limit)
            if done:
                break
        # If we tried every neighbor and didn't find a valid path, backtrack
        if not done:
            path.pop()
            current_vertex.color = "white"
    # If we visited the required number of nodes, we were successful!
    else:
        done = True
    # done will be False if we hit a dead end, or True if we found a valid path
    return done


if __name__ == "__main__":
    main()
