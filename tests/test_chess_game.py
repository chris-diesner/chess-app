import unittest
from chess_game import ChessGame
from figures.pawn import Pawn
from figures.rook import Rook
from figures.king import King
from figures.queen import Queen
from figures.knight import Knight

class TestChessGame(unittest.TestCase):
    
    def setUp(self):
        self.game = ChessGame()

    def test_white_opens_game_should_retrun_string_white(self):
        self.assertEqual(self.game.current_player, "white")

    def test_switch_player_should_return_string_switched_color(self):
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "black")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "white")
    
    def test_convert_to_coordinates_should_return_string_coordinates(self):
        result = self.game.convert_to_coordinates((0, 0))
        self.assertEqual(result, "A8")
        result = self.game.convert_to_coordinates((7, 7))
        self.assertEqual(result, "H1")
        
    def test_is_king_in_check_when_king_is_in_check_should_return_true_and_list_of_attacker_and_its_position(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        result, attacking_figures = self.game.is_king_in_check("black")
        self.assertTrue(result)
        self.assertEqual(len(attacking_figures), 1)
        self.assertIsInstance(attacking_figures[0][0], Rook)
        self.assertEqual(attacking_figures[0][0].color, "white")
        self.assertEqual(attacking_figures[0][1], (0, 7))
        
    def test_is_king_in_check_when_king_is_in_check_should_return_true_and_list_of_attackers_and_its_positions(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        self.game.board.fields[7][7] = Queen("white", (7, 7))
        result, attacking_figures = self.game.is_king_in_check("black")
        self.assertTrue(result)
        self.assertEqual(len(attacking_figures), 2)
        self.assertIsInstance(attacking_figures[0][0], Rook)
        self.assertEqual(attacking_figures[0][0].color, "white")
        self.assertEqual(attacking_figures[0][1], (0, 7))
        self.assertIsInstance(attacking_figures[1][0], Queen)
        self.assertEqual(attacking_figures[1][0].color, "white")
        self.assertEqual(attacking_figures[1][1], (7, 7))
        
    def test_is_king_in_check_when_king_is_not_in_check_should_return_false_and_empty_list_of_attackers(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][3] = King("black", (0, 3))
        self.game.board.fields[1][5] = Rook("white", (1, 5))
        result, attacking_figures = self.game.is_king_in_check("black")
        self.assertFalse(result)
        self.assertEqual(len(attacking_figures), 0)
        
    def test_is_king_in_checkmate_should_return_true(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        self.game.board.fields[1][7] = Queen("white", (1, 7))
        result = self.game.is_king_in_checkmate("black")
        self.assertTrue(result)

    def test_is_king_in_checkmate_should_return_false_if_king_can_escape(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        self.game.board.fields[1][1] = Rook("black", (1, 1))
        result = self.game.is_king_in_checkmate("black")
        self.assertFalse(result)

    def test_is_king_in_checkmate_should_return_false_if_attacker_can_be_taken(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        self.game.board.fields[1][7] = Rook("black", (1, 7))
        result = self.game.is_king_in_checkmate("black")
        self.assertFalse(result)
    
    def test_is_king_in_checkmate_should_return_false_if_attacker_can_be_blocked(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        #eig. Koenig blockieren
        self.game.board.fields[1][0] = Pawn("black", (1, 0))
        self.game.board.fields[0][1] = Pawn("black", (0, 1))
        self.game.board.fields[1][6] = Rook("black", (1, 6))
        result = self.game.is_king_in_checkmate("black")
        self.assertFalse(result)
        
    def test_is_king_in_checkmate_should_return_false_if_knight_blocks_attacker_and_king_cannot_escape(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("black", (0, 0))
        self.game.board.fields[0][7] = Rook("white", (0, 7))
        #eig. Koenig blockieren
        self.game.board.fields[1][0] = Pawn("black", (1, 0))
        self.game.board.fields[0][1] = Pawn("black", (0, 1))
        self.game.board.fields[2][1] = Knight("black", (2, 1))
        result = self.game.is_king_in_checkmate("black")
        self.assertFalse(result)

    def test_move_no_figure_should_return_string_empty_field(self):
        result = self.game.move_figure((3, 3), (4, 4))
        self.assertEqual(result, "Du hast ein leeres Feld ausgewählt!")
        print(f"Zug von (3, 3) nach (4, 4): {result}")

    def test_move_wrong_player_should_return_string_invalid_figure(self):
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertEqual(result, "Es ist white's Zug!")
        print(f"Zug von (6, 0) nach (4, 0): {result}")

    def test_invalid_move_should_return_string_invalid_move(self):
        result = self.game.move_figure((1, 0), (3, 1))
        self.assertEqual(result, "Ungültiger Zug!")
        print(f"Zug von (1, 0) nach (3, 1): {result}")

    def test_valid_move_should_return_string_movement_notation(self):
        result = self.game.move_figure((1, 0), (3, 0))
        expected_output = "Bauer (weiß) von A7 auf A5"
        self.assertEqual(result, expected_output)
        print(f"Zug von (1, 0) nach (3, 0): {result}")

    def test_valid_move_updates_board_should_return_string_updated_board(self):
        self.game.move_figure((1, 0), (3, 0))
        self.assertIsNone(self.game.board.fields[1][0])
        self.assertIsNotNone(self.game.board.fields[3][0])
        print("Brett nach Zug:")
        self.game.print_board()

    def test_valid_move_switches_player_shold_return_string_sitched_color_black(self):
        self.game.move_figure((1, 0), (3, 0))
        self.assertEqual(self.game.current_player, "black")
        print(f"Aktueller Spieler nach Zug: {self.game.current_player}")
        
    def test_capture_opponent_rook_with_own_pawn_should_return_string_valid_move_and_replaced_figure(self):
        self.game.board.fields[2][1] = Rook("black", (2, 1)) #gegn. Turm platzieren
        print("Brett vor Zug:")
        self.game.print_board() #debugging only - kann entfernt werden
        result = self.game.move_figure((1, 0), (2, 1))
        expected_output = "Bauer (weiß) schlägt Turm (schwarz) von A7 auf B6"
        self.assertEqual(result, expected_output)
        print(f"Zug von (1, 0) nach (2, 1) (Schlagen): {result}")
        self.assertIsInstance(self.game.board.fields[2][1], Pawn)
        self.assertEqual(self.game.board.fields[2][1].color, "white")
        self.assertIsNone(self.game.board.fields[1][0])
        print("Brett nach Zug:")
        self.game.print_board()

    def test_move_pawn_on_blocked_field_should_string_invalid_move(self):
        self.game.board.fields[2][1] = Rook("white", (2, 1)) #eig. Turm platzieren
        result = self.game.move_figure((1, 0), (2, 1))
        self.assertEqual(result, "Ungültiger Zug!")
        print(f"Zug von (1, 0) nach (2, 1) (eigene Figur): {result}")
        self.assertIsInstance(self.game.board.fields[2][1], Rook) #eig. Turm bleibt
        self.assertIsNotNone(self.game.board.fields[1][0])

    def test_capture_empty_field_should_return_string_invalid_move(self):
        result = self.game.move_figure((1, 0), (2, 1))  
        self.assertEqual(result, "Ungültiger Zug!")
        print(f"Zug von (1, 0) nach (2, 1) (leeres Feld): {result}")
        self.assertIsNone(self.game.board.fields[2][1])
        self.assertIsNotNone(self.game.board.fields[1][0])
        
    def test_move_while_in_check_should_return_string_invalid_move(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[1][0] = King("white", (1, 0))
        self.game.board.fields[0][7] = Rook("black", (0, 7))
        result = self.game.move_figure((1, 0), (0, 0))
        self.assertEqual(result, "ungültiger Zug! König im Schach!")
        
    def test_is_stalemate_should_return_true_if_no_legal_move_possible(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("white", (0, 0))
        self.game.board.fields[1][2] = King("black", (1, 2))
        self.game.board.fields[2][2] = Knight("black", (2, 2))
        self.game.current_player = "black"
        self.game.switch_player()
        self.assertTrue(self.game.check_stalemate())
        
    def test_is_stalemate_should_return_false_if_legal_moves_exist(self):
        self.game.board.fields = [[None for _ in range(8)] for _ in range(8)]
        self.game.board.fields[0][0] = King("white", (0, 0))
        self.game.board.fields[7][7] = King("black", (7, 7))
        self.game.board.fields[6][6] = Queen("white", (6, 6))
        self.game.board.fields[5][5] = Pawn("black", (5, 5))
        self.game.current_player = "white"
        self.game.switch_player()
        self.assertFalse(self.game.check_stalemate())

if __name__ == "__main__":
    unittest.main()
