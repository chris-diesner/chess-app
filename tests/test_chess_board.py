import unittest
from chess_board import ChessBoard  # Importiere die ChessBoard-Klasse aus deiner Hauptdatei

class TestChessBoard(unittest.TestCase):

    def setUp(self):
        """Setzt ein neues Schachbrett für jeden Test."""
        self.board = ChessBoard()

    def test_initial_setup(self):
        """Testet, ob das Schachbrett richtig initialisiert wurde."""
        # Erwartung: Es gibt insgesamt 32 Figuren (16 pro Seite)
        total_pieces = sum(1 for row in self.board.fields for cell in row if cell != " ")
        self.assertEqual(total_pieces, 32, "Initiales Setup sollte 32 Figuren enthalten")

    def test_pawns_position(self):
        """Testet, ob alle Bauern an der richtigen Position stehen."""
        # Erwartung: Die weißen Bauern sind in der zweiten Reihe (index 1)
        for i in range(8):
            self.assertEqual(self.board.fields[1][i], "P", f"Weißer Bauer fehlt auf Position (1, {i})")
            self.assertEqual(self.board.fields[6][i], "p", f"Schwarzer Bauer fehlt auf Position (6, {i})")

    def test_display_board(self):
        """Testet, ob die print_board-Methode ohne Fehler läuft."""
        try:
            self.board.print_board()
        except Exception as e:
            self.fail(f"print_board() hat einen Fehler verursacht: {e}")

# Führt die Tests aus, wenn das Skript direkt aufgerufen wird
if __name__ == '__main__':
    unittest.main()
