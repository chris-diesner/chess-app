import unittest
from figures.bishop import Bishop

class TestBishop(unittest.TestCase):
    
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_bishop = Bishop("white", (0, 2))
        self.black_bishop = Bishop("black", (7, 5))
        
    def test_valid_move_diagonal_should_return_true(self):
        self.assertTrue(self.white_bishop.is_move_valid((0, 2), (2, 0), self.board))
        self.assertTrue(self.black_bishop.is_move_valid((7, 5), (5, 7), self.board))
    
    def test_invalid_move_not_diagonal_should_return_false(self):
        self.assertFalse(self.white_bishop.is_move_valid((0, 2), (0, 0), self.board))
        self.assertFalse(self.black_bishop.is_move_valid((7, 5), (7, 7), self.board))
        
    def test_blocked_move_should_return_false(self):
        self.board[1][1] = Bishop("white", (1, 1))
        self.assertFalse(self.white_bishop.is_move_valid((0, 2), (2, 0), self.board))
        self.board[6][4] = Bishop("black", (6, 4))
        self.assertFalse(self.black_bishop.is_move_valid((7, 5), (5, 3), self.board))
        
    def test_capture_opponent_should_return_true(self):
        self.board[2][0] = Bishop("black", (2, 0))
        self.assertTrue(self.white_bishop.is_move_valid((0, 2), (2, 0), self.board))
        self.board[5][7] = Bishop("white", (5, 7))
        self.assertTrue(self.black_bishop.is_move_valid((7, 5), (5, 7), self.board))
        
    def test_out_of_bounds_move_should_return_false(self):
        self.assertFalse(self.white_bishop.is_move_valid((0, 2), (8, 2), self.board))
        self.assertFalse(self.black_bishop.is_move_valid((7, 5), (-1, 5), self.board))

if __name__ == "__main__":
    unittest.main()
