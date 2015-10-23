"""Board for a tic-tac-toe game."""

import itertools


# TODO: ValueError isn't the right exception type for some of these places.


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

    def _winner(self):

        rows = [[(x, y) for y in range(3)] for x in range(3)]
        cols = [[(x, y) for x in range(3)] for y in range(3)]
        diags = [[(0,0), (1,1), (2,2)], [(2,0), (1,1), (0,2)]]

        sets = rows + cols + diags
        print sets

        for set_pos in sets:
            cells = [self._board.get(pos, None) for pos in set_pos]
            print cells

            if all(map(lambda cell: cell == Board.X, cells)):
                return Board.X
            elif all(map(lambda cell: cell == Board.O, cells)):
                return Board.O

        return None



    def next_players(self):
        """Returns possible next players as list."""

        x_count = len([cell for pos, cell in self._board.iteritems() if cell == Board.X])
        o_count = len([cell for pos, cell in self._board.iteritems() if cell == Board.O])

        if not -1 <= x_count - o_count <= 1:
            return []  # not a valid board, maybe raise?

        if self._winner() is not None:
            return []

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

    def make_move(self, player, pos):
        """Make a move for player at pos."""
        if player not in self.next_players():
            raise ValueError('Not turn of player %s' % player)

        if pos in self._board:
            raise ValueError('Position already occupied: %s' % pos)

        self._board[pos] = player



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
