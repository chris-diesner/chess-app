
from chess_board import ChessBoard
from pawn import Pawn
from user import User

class ChessGame:
    def __init__(self, white_name="User 1", black_name="User 2"):
        self.board = ChessBoard()
        self.board.setup_fields()
        self.current_player = "white"
        self.last_move = None
        self.white_player = User(white_name, "white")
        self.black_player = User(black_name, "black")

    def move_figure(self, start_pos, end_pos):
        figure = self.board.fields[start_pos[0]][start_pos[1]]
        target_field = self.board.fields[end_pos[0]][end_pos[1]]

        if figure is None:
            return "You selected an empty square!"

        # Handle en passant
        if isinstance(figure, Pawn) and target_field is None:
            if abs(end_pos[1] - start_pos[1]) == 1:
                captured_pawn_row = start_pos[0] + (1 if figure.color == "white" else -1)
                captured_pawn = self.board.fields[captured_pawn_row][end_pos[1]]
                if isinstance(captured_pawn, Pawn) and captured_pawn.color != figure.color:
                    # Remove the captured pawn
                    self.board.fields[captured_pawn_row][end_pos[1]] = None

        # Perform the move
        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos

        # Track last move
        self.last_move = {
            "piece": figure,
            "start_pos": start_pos,
            "end_pos": end_pos,
            "two_square_pawn_move": isinstance(figure, Pawn) and abs(start_pos[0] - end_pos[0]) == 2,
        }

        # Switch player
        self.current_player = "black" if self.current_player == "white" else "white"
        return "Move completed!"
