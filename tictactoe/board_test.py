import unittest

from board import Board

board1 = '         '
board2 = ' xxo  o  '
board3 = 'oxxo  o  '
board4 = 'xo o   x '

invalid_board = 'xxxxxxxxx'

class BoardTest(unittest.TestCase):

    def test_wire_format_round_trip(self):
        self.assertEqual(Board(wire_format=board1).wire_format(), board1)
        self.assertEqual(Board(wire_format=board2).wire_format(), board2)
        self.assertEqual(Board(wire_format=board3).wire_format(), board3)
        self.assertEqual(Board(wire_format=board4).wire_format(), board4)

        # Maybe raise on init?
        self.assertEqual(Board(wire_format=invalid_board).wire_format(), invalid_board)


    def test_next_players(self):
        self.assertItemsEqual(['x', 'o'], Board(wire_format=board1).next_players())
        self.assertItemsEqual(['x', 'o'], Board(wire_format=board2).next_players())
        self.assertItemsEqual(['x'], Board(wire_format=board3).next_players())
        self.assertItemsEqual(['x', 'o'], Board(wire_format=board4).next_players())

        self.assertItemsEqual([], Board(wire_format=invalid_board).next_players())


if __name__ == '__main__':
    unittest.main()
