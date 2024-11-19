import unittest
from figures.queen import Queen

class TestQueen(unittest.TestCase):
    
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_queen = Queen("white", (0, 3))
        self.black_queen = Queen("black", (7, 3))

    def test_valid_horizontal_move_should_return_true(self):
        self.assertTrue(self.white_queen.is_move_valid((0, 3), (0, 7), self.board))
        self.assertTrue(self.black_queen.is_move_valid((7, 3), (7, 0), self.board))

    def test_valid_vertical_move_should_return_true(self):
        self.assertTrue(self.white_queen.is_move_valid((0, 3), (7, 3), self.board))
        self.assertTrue(self.black_queen.is_move_valid((7, 3), (0, 3), self.board))

    def test_valid_diagonal_move_should_return_true(self):
        self.assertTrue(self.white_queen.is_move_valid((0, 3), (4, 7), self.board))
        self.assertTrue(self.black_queen.is_move_valid((7, 3), (3, 7), self.board))

    def test_blocked_horizontal_move_should_return_false(self):
        self.board[0][5] = Queen("white", (0, 5))
        self.assertFalse(self.white_queen.is_move_valid((0, 3), (0, 7), self.board))

    def test_blocked_diagonal_move_should_return_false(self):
        self.board[4][4] = Queen("white", (4, 4))
        self.assertFalse(self.white_queen.is_move_valid((0, 3), (7, 0), self.board))

    def test_capture_opponent_should_return_true(self):
        self.board[0][7] = Queen("black", (0, 7))
        self.assertTrue(self.white_queen.is_move_valid((0, 3), (0, 7), self.board))

    def test_invalid_move_should_return_false(self):
        self.assertFalse(self.white_queen.is_move_valid((0, 3), (1, 5), self.board))

    def test_out_of_bounds_move_should_return_false(self):
        self.assertFalse(self.white_queen.is_move_valid((0, 3), (8, 3), self.board))
        self.assertFalse(self.white_queen.is_move_valid((0, 3), (-1, 3), self.board))

if __name__ == "__main__":
    unittest.main()
