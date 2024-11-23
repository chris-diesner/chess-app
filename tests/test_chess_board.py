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
        
    def test_notation_to_index_should_return_correct_matrix_indices(self):
        self.assertEqual(self.board.notation_to_index("A1"), (7, 0))
        self.assertEqual(self.board.notation_to_index("H8"), (0, 7))
        self.assertEqual(self.board.notation_to_index("D4"), (4, 3))
        self.assertEqual(self.board.notation_to_index("F6"), (2, 5))

    def test_pawns_position(self):
        for i in range(8):
            white_pawn = self.board.fields[6][i]
            black_pawn = self.board.fields[1][i]
            self.assertIsInstance(white_pawn, Pawn, f"Weißer Bauer fehlt auf Position (6, {i})")
            self.assertEqual(white_pawn.color, "white", f"Weißer Bauer hat falsche Farbe auf (6, {i})")
            self.assertIsInstance(black_pawn, Pawn, f"Schwarzer Bauer fehlt auf Position (1, {i})")
            self.assertEqual(black_pawn.color, "black", f"Schwarzer Bauer hat falsche Farbe auf (1, {i})")

    def test_major_pieces_position(self):
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, figure_class in enumerate(figures):
            white_piece = self.board.fields[7][i]
            black_piece = self.board.fields[0][i]
            self.assertIsInstance(white_piece, figure_class, f"Weiße {figure_class.__name__} fehlt auf Position (7, {i})")
            self.assertEqual(white_piece.color, "white", f"Weiße {figure_class.__name__} hat falsche Farbe auf (7, {i})")
            self.assertIsInstance(black_piece, figure_class, f"Schwarze {figure_class.__name__} fehlt auf Position (0, {i})")
            self.assertEqual(black_piece.color, "black", f"Schwarze {figure_class.__name__} hat falsche Farbe auf (0, {i})")

if __name__ == "__main__":
    unittest.main()
