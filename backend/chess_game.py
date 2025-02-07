from backend.chess_board import ChessBoard
from backend.figures.king import King
from backend.figures.pawn import Pawn
from backend.figures.queen import Queen
from backend.figures.rook import Rook
from backend.figures.knight import Knight
from backend.figures.bishop import Bishop
from backend.user import User
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)
board = ChessBoard()

@app.route('/api/board', methods=['GET'])
def get_board():
    return jsonify(board.get_board_state())

@app.route("/api/move", methods=["POST"])
def api_move_figure():
    data = request.get_json()
    
    game_id = data.get("gameId")
    figure_id = data.get("figureId")
    to_position = data.get("toPosition")

    if not game_id or not figure_id or not to_position:
        return jsonify({"error": "Fehlende Parameter"}), 400

    if game_id not in active_games:
        return jsonify({"error": "Spiel existiert nicht"}), 404

    game = active_games[game_id]

    # Finde die Figur anhand der UUID
    from_pos = None
    for row in range(8):
        for col in range(8):
            piece = game.board.fields[row][col]
            if piece and piece.id == figure_id:
                from_pos = (row, col)
                break
        if from_pos:
            break

    if not from_pos:
        return jsonify({"error": "Figur nicht gefunden"}), 404

    # Zielposition umwandeln (z. B. "e4" → (4,4))
    col_map = {letter: i for i, letter in enumerate("abcdefgh")}
    to_pos = (8 - int(to_position[1]), col_map[to_position[0]])

    # Figur bewegen
    move_result = game.move_figure(from_pos, to_pos, figure_id)

    if "Ungültiger Zug" in move_result:
        return jsonify({"error": move_result}), 400

    return jsonify({"message": "Zug erfolgreich", "board": game.get_board_state()})

class ChessGame:
    def __init__(self, white_name="User 1", black_name="User 2"):
        self.board = ChessBoard()
        self.board.setup_fields()
        self.current_player = "white"
        self.last_move = None
        self.white_player = User(white_name, "white")
        self.black_player = User(black_name, "black")

    def get_current_player(self):
        return self.white_player if self.current_player == "white" else self.black_player

    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
        if self.check_stalemate():
            print("Patt!")

    def check_stalemate(self):
        stalemate = self.is_stalemate(self.current_player)
        if stalemate:
            return True
        return False

    def convert_to_coordinates(self, pos):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        row = 8 - pos[0]
        column = columns[pos[1]]
        return f"{column}{row}"
    
    def get_king_position(self, player_color):
        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if isinstance(figure, King) and figure.color == player_color:
                    return (row, col)
        return None 

    def is_king_in_check(self, current_player):
        king_pos = self.get_king_position(current_player)
        if not king_pos:
            return False, None

        attacking_figures = []

        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if figure and figure.color != current_player:
                    if figure.is_move_valid((row, col), king_pos, self.board.fields):
                        attacking_figures.append((figure, (row, col)))

        return len(attacking_figures) > 0, attacking_figures

    def is_king_in_checkmate(self, current_player):
        king_in_check, attacking_figures = self.is_king_in_check(current_player)
        if not king_in_check:
            return False

        if len(attacking_figures) == 1:
            attacker_pos = attacking_figures[0][1]
            for row in range(8):
                for col in range(8):
                    figure = self.board.fields[row][col]
                    if figure and figure.color == current_player:
                        if figure.is_move_valid((row, col), attacker_pos, self.board.fields):
                            if not self.simulate_move_and_check(current_player, (row, col), attacker_pos):
                                return False

        king_pos = None
        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if isinstance(figure, King) and figure.color == current_player:
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        king = self.board.fields[king_pos[0]][king_pos[1]]
        for end_row in range(8):
            for end_col in range(8):
                if king.is_move_valid(king_pos, (end_row, end_col), self.board.fields):
                    if not self.simulate_move_and_check(current_player, king_pos, (end_row, end_col)):
                        return False
                    
        if len(attacking_figures) == 1:
            attacker_pos = attacking_figures[0][1]
            blocking_positions = self.get_positions_between(king_pos, attacker_pos)
            
            for row in range(8):
                for col in range(8):
                    figure = self.board.fields[row][col]
                    if figure and figure.color == current_player:
                        for block_pos in blocking_positions:
                            if figure.is_move_valid((row, col), block_pos, self.board.fields):
                                if not self.simulate_move_and_check(current_player, (row, col), block_pos):
                                    return False
        return True

    def simulate_move_and_check(self, current_player, start_pos, end_pos):
        temp_field = self.board.fields[end_pos[0]][end_pos[1]]
        figure = self.board.fields[start_pos[0]][start_pos[1]]

        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos

        still_in_check = self.is_king_in_check(current_player)[0]

        self.board.fields[start_pos[0]][start_pos[1]] = figure
        self.board.fields[end_pos[0]][end_pos[1]] = temp_field
        figure.position = start_pos

        return still_in_check
    
    def get_positions_between(self, start_pos, end_pos):
        positions = []
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                positions.append((start_row, col))
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                positions.append((row, start_col))
        elif abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if start_row < end_row else -1
            col_step = 1 if start_col < end_col else -1
            for i in range(1, abs(start_row - end_row)):
                positions.append((start_row + i * row_step, start_col + i * col_step))
        return positions

    def is_stalemate(self, current_player):
        king_in_check, _ = self.is_king_in_check(current_player)
        if king_in_check:
            return False
        
        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if figure and figure.color == current_player:
                    start_pos = (row, col)
                    for end_row in range(8):
                        for end_col in range(8):
                            end_pos = (end_row, end_col)
                            if figure.is_move_valid(start_pos, end_pos, self.board.fields):
                                if not self.simulate_move_and_check(current_player, start_pos, end_pos):
                                    return False
        return True
    
    def promote_pawn(self, position, promotion_choice):
        #aktuell nur mit queen weil keine user eingabe
        pawn = self.board.fields[position[0]][position[1]]
        if not isinstance(pawn, Pawn):
            raise ValueError("Nur pawnn sollten umgewandelt werden können.")
        if promotion_choice == "queen":
            promoted_figure = Queen(pawn.color, position)
        elif promotion_choice == "rook":
            promoted_figure = Rook(pawn.color, position)
        elif promotion_choice == "bishop":
            promoted_figure = Bishop(pawn.color, position)
        elif promotion_choice == "knight":
            promoted_figure = Knight(pawn.color, position)
        else:
            raise ValueError(f"Fehlerhaft Auswahl: {promotion_choice}")

        promoted_figure.id = pawn.id

        self.board.fields[position[0]][position[1]] = promoted_figure

        move_notation = (
            f"pawn ({pawn.color}, UUID: {pawn.id}) auf {self.convert_to_coordinates(position)} "
            f"zu {promotion_choice}"
        )
        self.get_current_player().record_move(move_notation)
        return move_notation
    
    def handle_rochade(self, king, start_pos, end_pos):
        if abs(start_pos[1] - end_pos[1]) != 2:
            return False
        #kurze oder lange Rochade
        row = start_pos[0]
        direction = 1 if end_pos[1] > start_pos[1] else -1 
        rook_col = 7 if direction == 1 else 0
        rook_target_col = 5 if direction == 1 else 3

        rook = self.board.fields[row][rook_col]
        if not isinstance(rook, Rook):
            return False

        if king.has_moved or rook.has_moved:
            return False

        positions_between = self.get_positions_between(start_pos, (row, rook_col))
        for position in positions_between:
            if self.board.fields[position[0]][position[1]] is not None:
                return False

        for col in range(start_pos[1], end_pos[1] + direction, direction):
            temp_king_pos = (row, col)
            if self.simulate_move_and_check(king.color, start_pos, temp_king_pos):
                return False

        self.board.fields[row][rook_col] = None
        self.board.fields[row][rook_target_col] = rook
        rook.position = (row, rook_target_col)

        self.board.fields[start_pos[0]][start_pos[1]] = None
        self.board.fields[end_pos[0]][end_pos[1]] = king
        king.position = end_pos

        move_notation = (
            f"Rochade {'kurz' if direction == 1 else 'lang'}: "
            f"King ({king.color}, UUID: {king.id}) and Rook ({rook.color}, UUID: {rook.id})"
        )
        self.get_current_player().record_move(move_notation)
        return True


    def move_figure(self, start_pos, end_pos, figure_id=None):
        if start_pos == end_pos:
            return "Ungültiger Zug: nicht auf das gleiche Feld ziehen!"
        figure = self.board.fields[start_pos[0]][start_pos[1]]
        target_field = self.board.fields[end_pos[0]][end_pos[1]]

        if figure is None:
            return "Du hast ein leeres Feld ausgewählt!"
        
        if figure_id and figure.id != figure_id:
            return "Fehler: Figuren-ID stimmt nicht überein!"
        
        if figure.color != self.current_player:
            return f"Es ist {self.current_player}'s Zug!"
        
        if isinstance(figure, King) and abs(start_pos[1] - end_pos[1]) == 2:
            if self.handle_rochade(figure, start_pos, end_pos):
                self.switch_player()
                return f"Rochade erfolgreich von {start_pos} nach {end_pos}"
            else:
                return "Ungültiger Zug: Rochade nicht erlaubt"
        
        if not figure.is_move_valid(start_pos, end_pos, self.board.fields, self.last_move):
            return "Ungültiger Zug!"
        
        if self.simulate_move_and_check(self.current_player, start_pos, end_pos):
            return "ungültiger Zug! king im Schach!"

        if target_field and target_field.color == figure.color:
            return "Ungültiger Zug! Zielfeld ist durch eine eigene Figur blockiert."
        
        id_validation_result = self.validate_target_id(target_field)
        if id_validation_result:
            return id_validation_result

        en_passant_notation = self.handle_en_passant(figure, start_pos, end_pos, target_field)
        if en_passant_notation:
            return en_passant_notation

        move_notation = self.generate_move_notation(figure, target_field, start_pos, end_pos)
        self.execute_move(figure, start_pos, end_pos, move_notation)

        if isinstance(figure, Pawn) and end_pos[0] in (0, 7):
            promotion_choice = self.get_current_player().choose_promotion()
            self.promote_pawn(end_pos, promotion_choice)

        self.last_move = {
            "figure": figure,
            "start_pos": start_pos,
            "end_pos": end_pos,
            "two_square_pawn_move": isinstance(figure, Pawn) and abs(start_pos[0] - end_pos[0]) == 2,
        }
        self.switch_player()
        return move_notation

    def validate_target_id(self, target_field):
        if target_field:
            last_move = self.get_last_move_or_set_start(target_field)
            if last_move and "UUID:" in last_move:
                uuid_start = last_move.find("UUID: ") + len("UUID: ")
                uuid_end = last_move.find(")", uuid_start)
                if uuid_start == -1 or uuid_end == -1:
                    return "Fehler: UUID nicht gefunden!"
                expected_target_uuid = last_move[uuid_start:uuid_end]
                if target_field.id != expected_target_uuid:
                    return "Fehler: UUID stimmen nicht überein!"
        return None

    def get_last_move_or_set_start(self, target_field):
        last_move = None
        if self.current_player == "black" and self.white_player.move_history:
            last_move = self.white_player.move_history[-1]
        elif self.current_player == "white" and self.black_player.move_history:
            last_move = self.black_player.move_history[-1]

        if not last_move or "UUID:" not in last_move:
            start_pos = target_field.position
            last_move = (
                f"{target_field.name} ({target_field.color}, UUID: {target_field.id}) "
                f"auf {self.convert_to_coordinates(start_pos)}"
            )
        return last_move

    def handle_en_passant(self, figure, start_pos, end_pos, target_field):
        if isinstance(figure, Pawn) and target_field is None:
            if abs(end_pos[1] - start_pos[1]) == 1: 
                captured_pawn_row = start_pos[0] 
                captured_pawn_col = end_pos[1]
                captured_pawn = self.board.fields[captured_pawn_row][captured_pawn_col]
                
                if (
                    isinstance(captured_pawn, Pawn)
                    and captured_pawn.color != figure.color
                    and self.last_move
                    and self.last_move["figure"] == captured_pawn
                    and self.last_move["two_square_pawn_move"]
                ):
                    self.board.fields[captured_pawn_row][captured_pawn_col] = None
                    
                    move_notation = (
                        f"{figure.name} ({figure.color}, UUID: {figure.id}) schlägt "
                        f"{captured_pawn.name} ({captured_pawn.color}, UUID: {captured_pawn.id}) "
                        f"en passant von {self.convert_to_coordinates(start_pos)} auf {self.convert_to_coordinates(end_pos)}"
                    )
                    
                    self.execute_move(figure, start_pos, end_pos, move_notation)
                    return move_notation
        return None

    def generate_move_notation(self, figure, target_field, start_pos, end_pos):
        if target_field is None:
            return (
                f"{figure.name} ({figure.color}, UUID: {figure.id}) "
                f"von {self.convert_to_coordinates(start_pos)} auf {self.convert_to_coordinates(end_pos)}"
            )
        else:
            return (
                f"{figure.name} ({figure.color}, UUID: {figure.id}) schlägt "
                f"{target_field.name} ({target_field.color}, UUID: {target_field.id}) "
                f"von {self.convert_to_coordinates(start_pos)} auf {self.convert_to_coordinates(end_pos)}"
            )

    def execute_move(self, figure, start_pos, end_pos, move_notation):
        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos
        self.get_current_player().record_move(move_notation)
        figure.move_history.append(move_notation)

    #Debugging Methoden
    def print_board(self):
        print(f"Am Zug: {self.current_player}")
        self.board.print_board()
        
    def print_move_history(self):
        print("Zug-Historie:")
        print("Weiß:")
        for i, move in enumerate(self.white_moves, 1):
            print(f"{i}. {move}")
        print("Schwarz:")
        for i, move in enumerate(self.black_moves, 1):
            print(f"{i}. {move}")
