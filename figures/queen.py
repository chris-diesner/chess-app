from figures.figure import Figure

class Queen(Figure):
    
    def is_move_valid(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        #Regel: Zuege nur innerhalb Spielfeld
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        #Regel: Dame bewegt sich horizontal, vertikal oder diagonal
        if start_row == end_row:
            step_row, step_col = 0, 1 if end_col > start_col else -1
        elif start_col == end_col:
            step_row, step_col = 1 if end_row > start_row else -1, 0
        elif abs(start_row - end_row) == abs(start_col - end_col):
            step_row = 1 if end_row > start_row else -1
            step_col = 1 if end_col > start_col else -1
        else:
            return False 

        #Regel: Dame darf keine Figuren überspringen
        row, col = start_row + step_row, start_col + step_col
        while (row, col) != (end_row, end_col):
            if board[row][col] is not None:
                return False
            row += step_row
            col += step_col

        #Regel: Zielfeld leer oder Gegner
        target_field = board[end_row][end_col]
        if target_field is None or target_field.color != self.color:
            return True

        return False
