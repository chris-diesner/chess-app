import unittest
from figures.pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        #weisser Bauer Startposition
        self.white_pawn = Pawn("white", (1, 1))
        #schwarzer Bauer Startposition
        self.black_pawn = Pawn("black", (6, 1))
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_single_forward_move_should_return_true(self):
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (2, 1), self.board))
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (5, 1), self.board))

    def test_double_forward_move_first_turn_should_return_true(self):
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (3, 1), self.board))
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (4, 1), self.board))

    def test_blocked_double_forward_move_should_return_false(self):
        self.board[2][1] = Pawn("white", (2, 1)) 
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (3, 1), self.board))

    def test_diagonal_capture_should_return_true(self):
        self.board[2][2] = Pawn("black", (2, 2)) 
        self.board[5][0] = Pawn("white", (5, 0)) 
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (2, 2), self.board)) 
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (5, 0), self.board)) 

    def test_invalid_diagonal_capture_empty_field_should_return_false(self):
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 2), self.board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 0), self.board))

    def test_invalid_diagonal_capture_own_piece_should_return_false(self):
        self.board[2][2] = Pawn("white", (2, 2)) 
        self.board[5][0] = Pawn("black", (5, 0)) 
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 2), self.board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 0), self.board))

    def test_blocked_forward_move(self):
        self.board[2][1] = Pawn("white", (2, 1))  
        self.board[5][1] = Pawn("black", (5, 1))  
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 1), self.board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 1), self.board))
        
    def test_out_of_bounds_move_should_return_false(self):
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (8, 1), self.board))
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (-1, 1), self.board))

if __name__ == "__main__":
    unittest.main()
