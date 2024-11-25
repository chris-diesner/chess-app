import unittest
from figures.pawn import Pawn
from figures.rook import Rook

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
        # Setup board state
        self.board[3][3] = Pawn("black", (3, 3))  # Black pawn at D5
        self.board[3][4] = Pawn("white", (3, 4))  # White pawn at E5

        # Mock last move: Black pawn moves from D7 to D5 (valid en passant scenario for white)
        last_move_black = {"figure": self.board[3][3], "start_pos": (1, 3), "end_pos": (3, 3)}
        print(last_move_black)

        # White pawn en passant to D6
        result = self.board[3][4].is_move_valid((3, 4), (2, 3), self.board, last_move_black)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_black}")
        self.assertTrue(result, "White pawn en passant to A5 failed")

        # Additional invalid en passant checks
        # Mock last move with incorrect positions
        invalid_last_move = {"figure": self.board[2][3], "start_pos": (2, 3), "end_pos": (3, 3)}

        result = self.board[3][4].is_move_valid((3, 4), (2, 3), self.board, invalid_last_move)
        self.assertFalse(result, "White pawn incorrectly validated for invalid last move")
        
    def test_en_passant_white_right_should_return_true_if_legal_move(self):
        # Setup board state
        self.board[3][2] = Pawn("black", (3, 2))  # Black pawn at C5
        self.board[3][1] = Pawn("white", (3, 1))  # White pawn at B5

        # Mock last move: Black pawn moves from C7 to DC (valid en passant scenario for white)
        last_move_black = {"figure": self.board[3][2], "start_pos": (1, 2), "end_pos": (3, 2)}
        print(last_move_black)

        # White pawn en passant to C6
        result = self.board[3][1].is_move_valid((3, 1), (2, 2), self.board, last_move_black)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_black}")
        self.assertTrue(result, "White pawn en passant to A5 failed")
    
    def test_en_passant_black_right_should_return_true_if_legal_move(self):
        # Setup board state
        self.board[4][3] = Pawn("white", (4, 3))  # White pawn at D4
        self.board[4][2] = Pawn("black", (4, 2))  # Black pawn at C4

        # Mock last move: White pawn moves from D2 to D4 (valid en passant scenario for black)
        last_move_white = {"figure": self.board[4][3], "start_pos": (6, 3), "end_pos": (4, 3)}
        print(last_move_white)

        # Black pawn en passant to D3
        result = self.board[4][2].is_move_valid((4, 2), (5, 3), self.board, last_move_white)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_white}")
        self.assertTrue(result, "Black pawn en passant to D3 failed")
        
    def test_en_passant_black_left_should_return_true_if_legal_move(self):
        # Setup board state
        self.board[4][4] = Pawn("white", (4, 4))  # White pawn at E4
        self.board[4][5] = Pawn("black", (4, 5))  # Black pawn at F4

        # Mock last move: White pawn moves from E2 to E4 (valid en passant scenario for black)
        last_move_white = {"figure": self.board[4][4], "start_pos": (6, 4), "end_pos": (4, 4)}
        print(last_move_white)

        # Black pawn en passant to E3
        result = self.board[4][5].is_move_valid((4, 5), (5, 4), self.board, last_move_white)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_white}")
        self.assertTrue(result, "Black pawn en passant to D3 failed")
        
    def test_en_passant_white_should_return_false_if_no_legal_condition(self):
        # Setup board state
        self.board[3][2] = Pawn("black", (3, 2))  # Black pawn at C5
        self.board[3][0] = Pawn("white", (3, 0))  # White pawn at A5

        # Mock last move: Black pawn moves from C7 to DC (valid en passant scenario for white)
        last_move_black = {"figure": self.board[3][2], "start_pos": (1, 2), "end_pos": (3, 2)}
        print(last_move_black)

        # White pawn en passant to B6
        result = self.board[3][0].is_move_valid((3, 0), (2, 1), self.board, last_move_black)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_black}")
        self.assertFalse(result, "White pawn incorrectly validated for invalid last move")
        
    def test_en_passant_black_should_return_false_if_no_legal_condition(self):
        # Setup board state
        self.board[4][2] = Pawn("white", (4, 2))  # White pawn at C4
        self.board[4][0] = Pawn("black", (4, 0))  # Black pawn at A4

        # Mock last move: White pawn moves from C2 to C4 (valid en passant scenario for black)
        last_move_white = {"figure": self.board[4][2], "start_pos": (6, 2), "end_pos": (4, 2)}
        print(last_move_white)

        # Black pawn en passant to B3
        result = self.board[4][0].is_move_valid((4, 0), (5, 1), self.board, last_move_white)
        print("DEBUG: Board Setup")
        for row in self.board:
            print(row)
        print(f"DEBUG: Last Move -> {last_move_white}")
        self.assertFalse(result, "Black pawn incorrectly validated for invalid last move")
        
    def test_en_passant_white_should_return_false_if_last_move_invalid(self):
        # Setup board state
        self.board[3][3] = Pawn("black", (3, 3))  # Black pawn at D5
        self.board[3][4] = Pawn("white", (3, 4))  # White pawn at E5


        # Mock last move: Black pawn moved incorrectly for en passant
        invalid_last_move = {"figure": self.board[2][3], "start_pos": (2, 3), "end_pos": (3, 3)}

        result = self.board[3][4].is_move_valid((3, 4), (2, 3), self.board, invalid_last_move)
        self.assertFalse(result, "White pawn incorrectly validated for invalid last move")

    def test_en_passant_black_should_return_false_if_last_move_invalid(self):
        # Setup board state
        self.board[4][3] = Pawn("black", (4, 3))  # Black pawn at D4
        self.board[4][4] = Pawn("white", (4, 4))  # White pawn at E4

        # Mock last move: White pawn moved incorrectly for en passant
        invalid_last_move = {"figure": self.board[5][4], "start_pos": (5, 4), "end_pos": (4, 4)}

        # Black pawn attempts en passant to E3
        result = self.board[4][3].is_move_valid((4, 3), (5, 4), self.board, invalid_last_move)
        self.assertFalse(result, "Black pawn incorrectly validated for invalid last move")

if __name__ == "__main__":
    unittest.main()
