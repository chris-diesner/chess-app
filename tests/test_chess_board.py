import unittest
from chess_board import ChessBoard

class TestChessBoard(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard()

    def test_initial_setup(self):
        total_pieces = sum(1 for row in self.board.fields for cell in row if cell != " ")
        self.assertEqual(total_pieces, 32, "Initiales Setup sollte 32 Figuren enthalten")

    def test_pawns_position(self):
        for i in range(8):
            self.assertEqual(self.board.fields[1][i], "P", f"Weißer Bauer fehlt auf Position (1, {i})")
            self.assertEqual(self.board.fields[6][i], "p", f"Schwarzer Bauer fehlt auf Position (6, {i})")

    def test_display_board(self):
        try:
            self.board.print_board()
        except Exception as e:
            self.fail(f"print_board() hat einen Fehler verursacht: {e}")