import unittest
from figures.pawn import Pawn
from figures.rook import Rook

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.white_pawn = Pawn("white", (6, 1))
        self.black_pawn = Pawn("black", (1, 1))
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_single_forward_move_should_return_true(self):
        print("DEBUG: Test einfacher Vorwärtszug")
        result = self.white_pawn.is_move_valid((6, 1), (5, 1), self.board)
        self.assertTrue(result)

        result = self.black_pawn.is_move_valid((1, 1), (2, 1), self.board)
        self.assertTrue(result)

    def test_double_forward_move_first_turn_should_return_true(self):
        print("DEBUG: Test Doppelschritt")
        result = self.white_pawn.is_move_valid((6, 1), (4, 1), self.board)
        self.assertTrue(result)

        result = self.black_pawn.is_move_valid((1, 1), (3, 1), self.board)
        self.assertTrue(result)

    def test_blocked_double_forward_move_should_return_false(self):
        print("DEBUG: Test blockierter Doppelschritt")
        self.board[5][1] = Pawn("white", (5, 1))
        result = self.white_pawn.is_move_valid((6, 1), (4, 1), self.board)
        self.assertFalse(result)

    def test_diagonal_capture_should_return_true(self):
        print("DEBUG: Test diagonaler Schlagzug")
        self.board[5][2] = Pawn("black", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertTrue(result)

    def test_invalid_diagonal_capture_empty_field_should_return_false(self):
        print("DEBUG: Test diagonaler Zug auf leeres Feld")
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)

    def test_invalid_diagonal_capture_own_piece_should_return_false(self):
        print("DEBUG: Test diagonaler Zug auf eigene Figur")
        self.board[5][2] = Pawn("white", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)

    def test_blocked_forward_move(self):
        print("DEBUG: Test blockierter Vorwärtszug")
        self.board[5][1] = Pawn("white", (5, 1))
        result = self.white_pawn.is_move_valid((6, 1), (5, 1), self.board)
        self.assertFalse(result)

    def test_out_of_bounds_move_should_return_false(self):
        print("DEBUG: Test Zug außerhalb des Bretts")
        result = self.white_pawn.is_move_valid((6, 1), (8, 1), self.board)
        self.assertFalse(result)

        result = self.white_pawn.is_move_valid((6, 1), (-1, 1), self.board)
        self.assertFalse(result)

    def test_invalid_direction_should_return_false(self):
        print("DEBUG: Test ungültige Richtung")
        result = self.white_pawn.is_move_valid((6, 1), (7, 1), self.board)
        self.assertFalse(result)

    def test_capture_own_piece_should_return_false(self):
        print("DEBUG: Test diagonaler Zug auf eigene Figur")
        self.board[5][2] = Rook("white", (5, 2))
        result = self.white_pawn.is_move_valid((6, 1), (5, 2), self.board)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
