import unittest
from backend.figures.pawn import Pawn
from backend.figures.rook import Rook

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.white_pawn = Pawn("white", (6, 1))
        self.black_pawn = Pawn("black", (1, 1))
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_single_forward_move_should_return_true(self):
        result = self.white_pawn.is_move_valid((6, 1), (5, 1), self.board)
        self.assertTrue(result)
        result = self.black_pawn.is_move_valid((1, 1), (2, 1), self.board)
        self.assertTrue(result)

    def test_double_forward_move_first_turn_should_return_true(self):
        result = self.white_pawn.is_move_valid((6, 1), (4, 1), self.board)
        self.assertTrue(result)

        result = self.black_pawn.is_move_valid((1, 1), (3, 1), self.board)
        self.assertTrue(result)

    def test_blocked_double_forward_move_should_return_false(self):
        self.board[5][1] = Pawn("white", (5, 1))
        result = self.white_pawn.is_move_valid((6, 1), (4, 1), self.board)
        self.assertFalse(result)

    def test_diagonal_capture_should_return_true(self):
        self.board[5][2] = Pawn("black", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertTrue(result)

    def test_invalid_diagonal_capture_empty_field_should_return_false(self):
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)

    def test_invalid_diagonal_capture_own_piece_should_return_false(self):
        self.board[5][2] = Pawn("white", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)

    def test_blocked_forward_move(self):
        self.board[5][1] = Pawn("white", (5, 1))
        result = self.white_pawn.is_move_valid((6, 1), (5, 1), self.board)
        self.assertFalse(result)

    def test_out_of_bounds_move_should_return_false(self):
        result = self.white_pawn.is_move_valid((6, 1), (8, 1), self.board)
        self.assertFalse(result)

        result = self.white_pawn.is_move_valid((6, 1), (-1, 1), self.board)
        self.assertFalse(result)

    def test_invalid_direction_should_return_false(self):
        result = self.white_pawn.is_move_valid((6, 1), (7, 1), self.board)
        self.assertFalse(result)

    def test_capture_own_piece_should_return_false(self):
        self.board[5][2] = Rook("white", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)
    
    def test_en_passant_white_left_should_return_true_if_legal_move(self):
        self.board[3][3] = Pawn("black", (3, 3)) 
        self.board[3][4] = Pawn("white", (3, 4))
        #Mock last move
        last_move_black = {"figure": self.board[3][3], "start_pos": (1, 3), "end_pos": (3, 3)}
        result = self.board[3][4].is_move_valid((3, 4), (2, 3), self.board, last_move_black)
        self.assertTrue(result)

    def test_en_passant_white_right_should_return_true_if_legal_move(self):
        self.board[3][2] = Pawn("black", (3, 2))
        self.board[3][1] = Pawn("white", (3, 1))
        #Mock last move
        last_move_black = {"figure": self.board[3][2], "start_pos": (1, 2), "end_pos": (3, 2)}
        result = self.board[3][1].is_move_valid((3, 1), (2, 2), self.board, last_move_black)
        self.assertTrue(result)
    
    def test_en_passant_black_right_should_return_true_if_legal_move(self):
        self.board[4][3] = Pawn("white", (4, 3))
        self.board[4][2] = Pawn("black", (4, 2))
        #Mock last move
        last_move_white = {"figure": self.board[4][3], "start_pos": (6, 3), "end_pos": (4, 3)}
        result = self.board[4][2].is_move_valid((4, 2), (5, 3), self.board, last_move_white)
        self.assertTrue(result)
        
    def test_en_passant_black_left_should_return_true_if_legal_move(self):
        self.board[4][4] = Pawn("white", (4, 4))
        self.board[4][5] = Pawn("black", (4, 5))
        #Mock last move
        last_move_white = {"figure": self.board[4][4], "start_pos": (6, 4), "end_pos": (4, 4)}
        result = self.board[4][5].is_move_valid((4, 5), (5, 4), self.board, last_move_white)
        self.assertTrue(result)
        
    def test_en_passant_white_should_return_false_if_no_legal_condition(self):
        self.board[3][2] = Pawn("black", (3, 2))
        self.board[3][0] = Pawn("white", (3, 0))
        #Mock last move
        last_move_black = {"figure": self.board[3][2], "start_pos": (1, 2), "end_pos": (3, 2)}
        result = self.board[3][0].is_move_valid((3, 0), (2, 1), self.board, last_move_black)
        self.assertFalse(result)
        
    def test_en_passant_black_should_return_false_if_no_legal_condition(self):
        self.board[4][2] = Pawn("white", (4, 2))
        self.board[4][0] = Pawn("black", (4, 0))
        #Mock last move
        last_move_white = {"figure": self.board[4][2], "start_pos": (6, 2), "end_pos": (4, 2)}
        result = self.board[4][0].is_move_valid((4, 0), (5, 1), self.board, last_move_white)
        self.assertFalse(result)
        
    def test_en_passant_white_should_return_false_if_last_move_invalid(self):
        self.board[3][3] = Pawn("black", (3, 3))
        self.board[3][4] = Pawn("white", (3, 4))
        #Mock inv. last move
        invalid_last_move = {"figure": self.board[2][3], "start_pos": (2, 3), "end_pos": (3, 3)}
        result = self.board[3][4].is_move_valid((3, 4), (2, 3), self.board, invalid_last_move)
        self.assertFalse(result)

    def test_en_passant_black_should_return_false_if_last_move_invalid(self):
        self.board[4][3] = Pawn("black", (4, 3))
        self.board[4][4] = Pawn("white", (4, 4))
        #Mock inv. last move
        invalid_last_move = {"figure": self.board[5][4], "start_pos": (5, 4), "end_pos": (4, 4)}
        result = self.board[4][3].is_move_valid((4, 3), (5, 4), self.board, invalid_last_move)
        self.assertFalse(result, "Black pawn incorrectly validated for invalid last move")

if __name__ == "__main__":
    unittest.main()
