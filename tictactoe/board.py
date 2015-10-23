"""Board for a tic-tac-toe game."""

import itertools


class Board(object):

    X = 'x'
    O = 'o'

    ALL_POSITIONS = list(itertools.product(range(3), range(3)))

    # Internal representation is dict of pairs (x, y); 0-indexed.
    __slots__ = ['_board']

    def __init__(self, wire_format=None):
        """Initialise a Board.

        Args:
          str_board: str, wire format representation of board from specs
        """
        if wire_format is not None:
            self._board = _parse_wire_format(wire_format)
        else:
            self._board = dict()

    def next_players(self):
        """Returns possible next players as list."""

        x_count = len([cell for pos, cell in self._board.iteritems() if cell == Board.X])
        o_count = len([cell for pos, cell in self._board.iteritems() if cell == Board.O])

        if not -1 <= x_count - o_count <= 1:
            return []  # not a valid board, maybe raise?

        if x_count == o_count:
            return [Board.X, Board.O]

        elif x_count > o_count:
            return [Board.O]
        else:
            return [Board.X]

    def pretty_print(self):
        """Formats the board for presentation as fixed-width text."""
        raise NotImplementedError()

    def wire_format(self):
        """Formats the board in wire format from spec."""
        cells = []
        for x in range(3):
            for y in range(3):
                cells.append(self._board.get((x, y), ' '))

        return ''.join(cells)

    def available_moves(self, player):
        """Returns list of available positions to play in for player.

        Args:
          player: the player to check moves for

        Raises:
          ValueError: if it is not possibly player's turn
        """
        if player not in self.next_players():
            raise ValueError('Not turn of player %s' % player)

        return filter(lambda pos: pos not in self._board, Board.ALL_POSITIONS)


def _parse_wire_format(wire_format):
    """Parses a wire format board to internal representation."""

    if not len(wire_format) == 9:
        raise ValueError('Invalid wire format board: %s' % wire_format)

    rows = wire_format[:3], wire_format[3:6], wire_format[6:9]

    board_rep = dict()
    for x, row in enumerate(rows):
        for y, cell in enumerate(row):
            if cell == 'x':
                board_rep[(x,y)] = Board.X
            elif cell == 'o':
                board_rep[(x,y)] = Board.O
            elif cell == ' ':
                pass
            else:
                raise ValueError('Invalid character in wire format: %s' % cell)

    return board_rep



    return dict()
