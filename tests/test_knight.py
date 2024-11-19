# tests/test_knight.py

import unittest
from figures.knight import Knight

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_knight = Knight("white", (0, 1))
        self.black_knight = Knight("black", (7, 1))

    def test_valid_knight_moves_should_return_true(self):
        self.assertTrue(self.white_knight.is_move_valid((0, 1), (2, 0), self.board))
        self.assertTrue(self.white_knight.is_move_valid((0, 1), (2, 2), self.board))

    def test_invalid_knight_moves_should_return_false(self):
        self.assertFalse(self.white_knight.is_move_valid((0, 1), (0, 3), self.board))
        self.assertFalse(self.black_knight.is_move_valid((7, 1), (5, 3), self.board))

    def test_capture_opponent_should_return_true(self):
        self.board[2][0] = Knight("black", (2, 0))
        self.assertTrue(self.white_knight.is_move_valid((0, 1), (2, 0), self.board))

    def test_out_of_bounds_move_should_return_false(self):
        self.assertFalse(self.white_knight.is_move_valid((0, 1), (2, -1), self.board))

if __name__ == "__main__":
    unittest.main()
