import unittest
from chess_game import ChessGame
from figures.pawn import Pawn
from figures.rook import Rook
from figures.king import King
from figures.queen import Queen


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

if __name__ == "__main__":
    unittest.main()
