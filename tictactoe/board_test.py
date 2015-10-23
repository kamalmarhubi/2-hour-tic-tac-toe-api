import unittest

from board import Board


class BoardTest(unittest.TestCase):

    def test_wire_format_round_trip(self):
        board1 = '         '
        self.assertEqual(Board(wire_format=board1).wire_format(), board1)

        board2 = ' xxo  o  '
        self.assertEqual(Board(wire_format=board2).wire_format(), board2)

        board3 = 'oxxo  o  '
        self.assertEqual(Board(wire_format=board3).wire_format(), board3)

        board4 = 'xo o   x '
        self.assertEqual(Board(wire_format=board4).wire_format(), board4)


if __name__ == '__main__':
    unittest.main()
