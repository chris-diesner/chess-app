import unittest
from figures.pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        #weisser Bauer Startpositon
        self.white_pawn = Pawn("white", (1, 1))
        #schwarzer Bauer Startposition
        self.black_pawn = Pawn("black", (6, 1))

    def test_single_forward_move_should_return_true(self):
        """Testet, ob der Bauer ein Feld nach vorne ziehen kann."""
        board = [[None for _ in range(8)] for _ in range(8)]  # Leeres Brett
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (2, 1), board))
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (5, 1), board))

    def test_double_forward_move_first_turn_should_return_true(self):
        """Testet, ob der Bauer zwei Felder nach vorne ziehen kann (erster Zug)."""
        board = [[None for _ in range(8)] for _ in range(8)]  # Leeres Brett
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (3, 1), board))
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (4, 1), board))

    def test_blocked_double_forward_move_should_return_false(self):
        """Testet, ob der doppelte Zug blockiert wird, wenn ein Hindernis im Weg ist."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][1] = Pawn("white", (2, 1))  # Blockiert das Feld vor dem weißen Bauern
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (3, 1), board))

    def test_diagonal_capture_should_return_true(self):
        """Testet, ob der Bauer diagonal schlagen kann."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][2] = Pawn("black", (2, 2))  # Gegnerischer Bauer
        board[5][0] = Pawn("white", (5, 0))  # Gegnerischer Bauer
        self.assertTrue(self.white_pawn.is_move_valid((1, 1), (2, 2), board))  # Weiß schlägt Schwarz
        self.assertTrue(self.black_pawn.is_move_valid((6, 1), (5, 0), board))  # Schwarz schlägt Weiß

    def test_invalid_diagonal_capture_empty_field_should_return_false(self):
        """Testet, dass der Bauer nicht diagonal ziehen kann, wenn das Zielfeld leer ist."""
        board = [[None for _ in range(8)] for _ in range(8)]  # Leeres Brett
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 2), board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 0), board))

    def test_invalid_diagonal_capture_own_piece_should_return_false(self):
        """Testet, dass der Bauer keine eigene Figur schlagen kann."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][2] = Pawn("white", (2, 2))  # Eigener Bauer für Weiß
        board[5][0] = Pawn("black", (5, 0))  # Eigener Bauer für Schwarz
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 2), board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 0), board))

    def test_blocked_forward_move(self):
        """Testet, ob der Bauer nicht ziehen kann, wenn das Zielfeld blockiert ist."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[2][1] = Pawn("white", (2, 1))  # Blockiert das Zielfeld vor dem weißen Bauern
        board[5][1] = Pawn("black", (5, 1))  # Blockiert das Zielfeld vor dem schwarzen Bauern
        self.assertFalse(self.white_pawn.is_move_valid((1, 1), (2, 1), board))
        self.assertFalse(self.black_pawn.is_move_valid((6, 1), (5, 1), board))

if __name__ == "__main__":
    unittest.main()
