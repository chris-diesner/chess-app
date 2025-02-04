import unittest
from backend.figures.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_king = King("white", (0, 4))
        self.black_king = King("black", (7, 4))

    def test_valid_king_moves_should_return_true(self):
        self.assertTrue(self.white_king.is_move_valid((0, 4), (1, 4), self.board))
        self.assertTrue(self.white_king.is_move_valid((0, 4), (1, 5), self.board))
        self.assertTrue(self.black_king.is_move_valid((7, 4), (6, 4), self.board))

    def test_invalid_king_moves_should_return_false(self):
        self.assertFalse(self.white_king.is_move_valid((0, 4), (2, 4), self.board))
        self.assertFalse(self.black_king.is_move_valid((7, 4), (5, 4), self.board))

    def test_capture_opponent_should_return_true(self):
        self.board[1][4] = King("black", (1, 4))
        self.assertTrue(self.white_king.is_move_valid((0, 4), (1, 4), self.board))

    def test_out_of_bounds_move_should_return_false(self):
        self.assertFalse(self.white_king.is_move_valid((0, 4), (-1, 4), self.board))

if __name__ == "__main__":
    unittest.main()
