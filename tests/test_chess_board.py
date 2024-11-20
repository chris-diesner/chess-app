import unittest
from chess_board import ChessBoard
from figures.pawn import Pawn
from figures.rook import Rook
from figures.knight import Knight
from figures.bishop import Bishop
from figures.queen import Queen
from figures.king import King

class TestChessBoard(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard()
        
    def test_initial_setup_debug(self):
        """Debug-Version: Testet die Initialisierung der Figuren."""
        for row in self.board.fields:
            print([type(cell).__name__ if cell else None for cell in row])


    def test_initial_setup(self):
        """Testet, ob das Brett korrekt initialisiert ist (32 Figuren)."""
        total_pieces = sum(1 for row in self.board.fields for cell in row if cell is not None)
        self.assertEqual(total_pieces, 32, "Initiales Setup sollte 32 Figuren enthalten")


    def test_pawns_position(self):
        """Testet, ob die Bauern korrekt positioniert sind."""
        for i in range(8):
            white_pawn = self.board.fields[1][i]
            black_pawn = self.board.fields[6][i]
            self.assertIsInstance(white_pawn, Pawn, f"Weißer Bauer fehlt auf Position (1, {i})")
            self.assertEqual(white_pawn.color, "white", f"Weißer Bauer hat falsche Farbe auf (1, {i})")
            self.assertIsInstance(black_pawn, Pawn, f"Schwarzer Bauer fehlt auf Position (6, {i})")
            self.assertEqual(black_pawn.color, "black", f"Schwarzer Bauer hat falsche Farbe auf (6, {i})")

    def test_major_pieces_position(self):
        """Testet, ob die Hauptfiguren (außer Bauern) korrekt positioniert sind."""
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, figure_class in enumerate(figures):
            white_piece = self.board.fields[0][i]
            black_piece = self.board.fields[7][i]
            self.assertIsInstance(white_piece, figure_class, f"Weiße {figure_class.__name__} fehlt auf Position (0, {i})")
            self.assertEqual(white_piece.color, "white", f"Weiße {figure_class.__name__} hat falsche Farbe auf (0, {i})")
            self.assertIsInstance(black_piece, figure_class, f"Schwarze {figure_class.__name__} fehlt auf Position (7, {i})")
            self.assertEqual(black_piece.color, "black", f"Schwarze {figure_class.__name__} hat falsche Farbe auf (7, {i})")

    def test_display_board(self):
        """Testet, ob die Ausgabe des Bretts funktioniert."""
        try:
            self.board.print_board()
        except Exception as e:
            self.fail(f"print_board() hat einen Fehler verursacht: {e}")

if __name__ == "__main__":
    unittest.main()
