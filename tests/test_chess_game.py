import unittest
from chess_game import ChessGame
from figures.pawn import Pawn
from figures.rook import Rook
from figures.knight import Knight
from figures.bishop import Bishop
from figures.queen import Queen
from figures.king import King

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
        result = self.game.move_figure((1, 0), (3, 0))
        self.assertEqual(result, "Es ist white's Zug!")
        print(f"Zug von (1, 0) nach (3, 0): {result}")

    def test_invalid_move_should_return_string_invalid_move(self):
        result = self.game.move_figure((6, 0), (3, 1))
        self.assertEqual(result, "Ungültiger Zug!")
        print(f"Zug von (6, 0) nach (3, 1): {result}")
        
    def test_valid_move_should_return_string_movement_notation(self):
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)

    def test_valid_move_updates_board_should_return_string_updated_board(self):
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)
        self.assertIsNone(self.game.board.fields[6][0])
        self.assertIsInstance(self.game.board.fields[4][0], Pawn)

    def test_valid_move_switches_player_shold_return_string_sitched_color_black(self):
        self.game.move_figure((6, 0), (4, 0)) 
        self.assertEqual(self.game.current_player, "black")

    def test_capture_opponent_with_uuid_should_return_string_valid_move(self):
        self.game.board.fields[5][1] = Rook("black", (5, 1))
        attacking_pawn = self.game.board.fields[6][0]
        result = self.game.move_figure((6, 0), (5, 1), attacking_pawn.id)
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("schlägt Turm (black", result)
        self.assertIsNone(self.game.board.fields[6][0]) 
        self.assertIsInstance(self.game.board.fields[5][1], Pawn) 

    def test_move_pawn_on_blocked_field_should_return_string_invalid_move(self):
        self.game.board.fields[5][0] = Pawn("white", (5, 0))
        result = self.game.move_figure((6, 0), (5, 0))
        self.assertEqual(result, "Ungültiger Zug!")

    def test_capture_empty_field_should_return_string_invalid_move(self):
        result = self.game.move_figure((6, 0), (5, 1)) 
        self.assertEqual(result, "Ungültiger Zug!")
        
    def test_move_while_in_check_should_return_string_invalid_move_king_check(self):
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
        
    def test_fools_mate(self):
        #Zug 1: weiß f2 -> f3
        self.game.move_figure((6, 5), (5, 5))
        self.assertEqual(self.game.current_player, "black")
        self.assertIsNone(self.game.board.fields[6][5])
        self.assertIsInstance(self.game.board.fields[5][5], Pawn)

        #Zug 2: schwarz e7 -> e5
        self.game.move_figure((1, 4), (3, 4)) 
        self.assertEqual(self.game.current_player, "white")
        self.assertIsNone(self.game.board.fields[1][4])
        self.assertIsInstance(self.game.board.fields[3][4], Pawn)

        #Zug 3: weiß g2 -> g4
        self.game.move_figure((6, 6), (4, 6)) 
        self.assertEqual(self.game.current_player, "black")
        self.assertIsNone(self.game.board.fields[6][6])
        self.assertIsInstance(self.game.board.fields[4][6], Pawn)

        #Zug 4: schwarz d8 -> h4
        self.game.move_figure((0, 3), (4, 7))
        self.assertEqual(self.game.current_player, "white")
        self.assertIsNone(self.game.board.fields[0][3])
        self.assertIsInstance(self.game.board.fields[4][7], Queen)

        is_checkmate = self.game.is_king_in_checkmate("white")
        self.assertTrue(is_checkmate)

    def test_move_with_invalid_uuid_should_return_error_mismatched_figure_ids(self):
        invalid_uuid = "00000000-0000-0000-0000-000000000000"
        result = self.game.move_figure((6, 0), (4, 0), invalid_uuid)
        self.assertEqual(result, "Fehler: Figuren-ID stimmt nicht überein!")

    def test_move_with_correct_uuid_should_should_return_string_valid_move(self):
        valid_uuid = self.game.board.fields[6][0].id
        result = self.game.move_figure((6, 0), (4, 0), valid_uuid)
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)
        
    def test_valid_move_should_return_string_movement_notation(self):
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)

    def test_valid_move_updates_board_should_return_string_updated_board(self):
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)
        self.assertIsNone(self.game.board.fields[6][0]) 
        self.assertIsInstance(self.game.board.fields[4][0], Pawn) 

    def test_capture_opponent_with_uuid_should_return_string_valid_move(self):
        self.game.board.fields[5][1] = Rook("black", (5, 1))
        attacking_pawn = self.game.board.fields[6][0]
        result = self.game.move_figure((6, 0), (5, 1), attacking_pawn.id)
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("schlägt Turm (black", result)
        self.assertIsNone(self.game.board.fields[6][0]) 
        self.assertIsInstance(self.game.board.fields[5][1], Pawn)
        self.assertEqual(self.game.board.fields[5][1].color, "white")
        white_moves = self.game.white_player.move_history
        self.assertEqual(len(white_moves), 1)
        self.assertIn("schlägt Turm (black", white_moves[0])
        self.assertIn(attacking_pawn.id, white_moves[0])

    def test_capture_opponent_rook_with_own_pawn_should_return_string_move_notation_and_replaced_figure(self):
        self.game.board.fields[5][1] = Rook("black", (5, 1))
        result = self.game.move_figure((6, 0), (5, 1))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("schlägt Turm (black", result)
        self.assertIsNone(self.game.board.fields[6][0])
        self.assertIsInstance(self.game.board.fields[5][1], Pawn)

    def test_move_with_correct_uuid_should_return_string_valid_move(self):
        valid_uuid = self.game.board.fields[6][0].id
        result = self.game.move_figure((6, 0), (4, 0), valid_uuid)
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von A2 auf A4", result)

    def test_move_history_should_return_list_move_history(self):
        self.game.move_figure((6, 5), (5, 5))  
        white_moves = self.game.white_player.move_history
        self.assertEqual(len(white_moves), 1)
        self.assertIn("von F2 auf F3", white_moves[0])
        self.game.move_figure((1, 4), (3, 4))
        black_moves = self.game.black_player.move_history
        self.assertEqual(len(black_moves), 1)
        self.assertIn("von E7 auf E5", black_moves[0])
        self.game.move_figure((6, 6), (4, 6))
        white_moves = self.game.white_player.move_history
        self.assertEqual(len(white_moves), 2)
        self.assertIn("von G2 auf G4", white_moves[1])
        self.game.move_figure((1, 3), (3, 3))
        black_moves = self.game.black_player.move_history
        self.assertEqual(len(black_moves), 2)
        self.assertIn("von D7 auf D5", black_moves[1])
    
    def test_move_wrong_player_should_return_string_invalid_figure(self):
        self.game.current_player = "black"
        result = self.game.move_figure((6, 0), (4, 0))
        self.assertEqual(result, "Es ist black's Zug!")
        
    def test_target_uuid_mismatch_should_return_error_for_mismatched_ids_in_history(self):
        self.game.move_figure((6, 0), (4, 0)) 
        self.game.move_figure((1, 4), (3, 4))
        self.game.board.fields[3][1] = Rook("black", (3, 1))
        attacking_pawn = self.game.board.fields[4][0] 
        result = self.game.move_figure((4, 0), (3, 1), attacking_pawn.id)
        self.assertEqual(result, "Ungültiger Zug: Ziel-UUID stimmt nicht mit der Zughistorie überein!")
        
    def test_legal_en_passant_rule_schould_return_valid_move_history(self):
        self.game.move_figure((6, 4), (4, 4))
        self.game.move_figure((1, 1), (2, 1))
        self.game.move_figure((4, 4), (3, 4))
        self.game.move_figure((1, 3), (3, 3))
        result = self.game.move_figure((3, 4), (2, 3))
        self.assertTrue(result.startswith("Bauer (white"))
        self.assertIn("von E5 auf D6", result)

if __name__ == "__main__":
    unittest.main()
