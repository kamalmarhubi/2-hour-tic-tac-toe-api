"""Board for a tic-tac-toe game."""


class Board(object):

    X = 'x'
    O = 'o'

    # Internal representation is dict of pairs (x, y); 0-indexed.
    __slots__ = ['board_']

    def __init__(self, wire_format=None):
        """Initialise a Board.

        Args:
          str_board: str, wire format representation of board from specs
        """
        if wire_format is not None:
            board_ = _parse_wire_format(wire_format)
        else:
            board_ = dict()

    def next_players(self):
        """Returns possible next players."""

        return []

    def pretty_print(self):
        """Formats the board for presentation as fixed-width text."""
        pass

    def wire_format(self):
        """Formats the board in wire format from spec."""
        pass


def _parse_wire_format(wire_format):
    """Parses a wire format board to internal representation."""
    return dict()
