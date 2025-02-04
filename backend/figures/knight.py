from backend.figures.figure import Figure

class Knight(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position, "knight")
        
    def is_move_valid(self, start_pos, end_pos, board, last_move=None):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        #Regel: knight bewegt sich in einem "L"-Muster
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_field = board[end_row][end_col]
            return target_field is None or target_field.color != self.color

        return False
