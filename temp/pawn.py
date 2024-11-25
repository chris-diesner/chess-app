
class Pawn(Figure):
    def __init__(self, color, position):
        super().__init__(color, position, "Bauer")
        
    def is_move_valid(self, start_pos, end_pos, board, last_move=None):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # En passant logic
        if last_move and isinstance(last_move["piece"], Pawn):
            if self.color == "white" and start_row == 3 and end_row == 2 and abs(end_col - start_col) == 1:
                if last_move["start_pos"] == (start_row + 2, end_col) and last_move["end_pos"] == (start_row, end_col):
                    return True
            elif self.color == "black" and start_row == 4 and end_row == 5 and abs(end_col - start_col) == 1:
                if last_move["start_pos"] == (start_row - 2, end_col) and last_move["end_pos"] == (start_row, end_col):
                    return True

        return False
