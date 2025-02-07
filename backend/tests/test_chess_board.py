import unittest
import uuid
from backend.chess_board import ChessBoard
from backend.figures.pawn import Pawn
from backend.figures.rook import Rook
from backend.figures.knight import Knight
from backend.figures.bishop import Bishop
from backend.figures.queen import Queen
from backend.figures.king import King
from backend.figures.figure import Figure

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
            self.assertIsInstance(white_pawn, Pawn)
            self.assertEqual(white_pawn.color, "white")
            self.assertIsInstance(black_pawn, Pawn)
            self.assertEqual(black_pawn.color, "black")

    def test_major_pieces_position(self):
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, figure_class in enumerate(figures):
            white_piece = self.board.fields[7][i]
            black_piece = self.board.fields[0][i]
            self.assertIsInstance(white_piece, figure_class)
            self.assertEqual(white_piece.color, "white")
            self.assertIsInstance(black_piece, figure_class)
            self.assertEqual(black_piece.color, "black")
            
    def test_figure_uuids(self):
        for row in self.board.fields:
            for figure in row:
                if figure is not None:
                    self.assertTrue(hasattr(figure, "id"))
                    self.assertIsInstance(uuid.UUID(figure.id), uuid.UUID)

if __name__ == "__main__":
    unittest.main()
