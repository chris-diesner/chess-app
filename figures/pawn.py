from figures.figure import Figure

class Pawn(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position, "Bauer")
        
    def is_move_valid(self, start_pos, end_pos, board, last_move=None):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # White pawn movement rules
        if self.color == "white":
            # Single forward move
            if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] is None:
                return True

            # Double forward move
            if start_row == 6 and end_row == start_row - 2 and start_col == end_col:
                if board[start_row - 1][start_col] is None and board[end_row][end_col] is None:
                    return True

            # Diagonal capture (including en passant)
            if end_row == start_row - 1 and abs(end_col - start_col) == 1:
                # Regular diagonal capture
                if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                    return True

                # En passant
                if last_move and isinstance(last_move["figure"], Pawn):
                    print("DEBUG: En passant last move details:")
                    print(f"  Last Move Start -> {last_move['start_pos']}, End -> {last_move['end_pos']}")
                    print("DEBUG: Checking white pawn en passant conditions")
                    if (
                        # Opponent moved two rows forward
                        last_move["start_pos"][0] == last_move["end_pos"][0] - 2 and  
                        # Current move targets the opponent's ending position diagonally
                        last_move["end_pos"] == (start_row, end_col)
                    ):
                        print("DEBUG: En passant conditions met for white pawn.")
                        return True

        # Black pawn movement rules
        if self.color == "black":
            # Single forward move
            if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            # Double forward move for black
            if start_row == 1 and end_row == start_row + 2 and start_col == end_col:
                if board[start_row + 1][start_col] is None and board[end_row][end_col] is None:
                    return True

            if end_row == start_row + 1 and abs(end_col - start_col) == 1:
                # Regular diagonal capture
                if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                    return True

                # En passant
                if last_move and isinstance(last_move["figure"], Pawn):
                    print("DEBUG: En passant last move details:")
                    print(f"  Last Move Start -> {last_move['start_pos']}, End -> {last_move['end_pos']}")
                    print("DEBUG: Checking black pawn en passant conditions")
                    if (
                        # Opponent moved two rows forward
                        last_move["start_pos"][0] == last_move["end_pos"][0] + 2 and  
                        # Current move targets the opponent's ending position diagonally
                        last_move["end_pos"] == (start_row, end_col)
                    ):
                        print("DEBUG: En passant conditions met for black pawn.")
                        return True

        return False
