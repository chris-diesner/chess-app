import unittest
from figures.bishop import Bishop

class TestBishop(unittest.TestCase):
    
    def setUp(self):
        self.white_bishop = Bishop("white", (0, 2))
        self.black_bishop = Bishop("black", (7, 5))
        
    def test_valid_move_diagonal_should_return_true(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        self.assertTrue(self.white_bishop.is_move_valid((0, 2), (2, 0), board))
        self.assertTrue(self.black_bishop.is_move_valid((7, 5), (5, 7), board))
    
    def test_invalid_move_not_diagonal_should_return_false(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        self.assertFalse(self.white_bishop.is_move_valid((0, 2), (0, 0), board))
        self.assertFalse(self.black_bishop.is_move_valid((7, 5), (7, 7), board))
        
    def test_blocked_move_should_return_false(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[1][1] = Bishop("white", (1, 1))  #hier steht eine Figur
        self.assertFalse(self.white_bishop.is_move_valid((0, 2), (2, 0), board))
        self.assertFalse(self.black_bishop.is_move_valid((2, 2), (0, 0), board))
        
    def test_capture_opponent_should_return_true(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][0] = Bishop("black", (2, 0))  #hier steht eine gegnerische Figur
        self.assertTrue(self.white_bishop.is_move_valid((0, 2), (2, 0), board))
        
if __name__ == "__main__":
    unittest.main()