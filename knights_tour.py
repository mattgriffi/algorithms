"""This program solves the Knight's Tour chess puzzle with a depth first search on a Graph."""


from data_structures.graph import Graph


def knight_graph(board_size):
    """Generates a graph representing all possible moves of a knight on a chess board of given
    width."""
    graph = Graph()

    for row in range(board_size):
        for col in range(board_size):
            current_node_id = position_to_node_id(row, col, board_size)
            legal_move_positions = generate_legal_moves(row, col, board_size)
            for position in legal_move_positions:
                legal_move_node_id = position_to_node_id(position[0], position[1], board_size)
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
