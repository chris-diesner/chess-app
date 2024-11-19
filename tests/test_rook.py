import unittest
from figures.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        self.white_rook = Rook("white", (0, 0))
        self.black_rook = Rook("white", (7, 7))
        
    def test_valid_move_horizontal_should_return_true(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        self.assertTrue(self.white_rook.is_move_valid((0, 0), (0, 7), board))
        
    def test_valid_vertical_move_should_return_true(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        self.assertTrue(self.black_rook.is_move_valid((7, 7), (0, 7), board))

    def test_blocked_move_should_return_false(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0][4] = Rook("white", (0, 4))  #hier steht eine Figur
        self.assertFalse(self.white_rook.is_move_valid((0, 0), (0, 7), board))

    def test_capture_opponent_should_return_true(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0][7] = Rook("black", (0, 7))  #hier steht eine gegnerische Figur
        self.assertTrue(self.white_rook.is_move_valid((0, 0), (0, 7), board))

    def test_invalid_diagonal_move_should_return_false(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        self.assertFalse(self.white_rook.is_move_valid((0, 0), (7, 7), board))

if __name__ == "__main__":
    unittest.main()