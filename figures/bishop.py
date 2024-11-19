from figures.figure import Figure

class Bishop(Figure):
    
    def is_move_valid(self, start_pos, end_pos, board):
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        #Regel: Laeufer bewegt sich nur diagonal
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        
        #Regel: Laeufer darf keine Figuren ueberspringen
        step_row = 1 if end_row > start_row else -1
        step_col = 1 if end_col > start_col else -1
        row, col = start_row + step_row, start_col + step_col
        while row != end_row:
            if board[row][col] is not None:
                return False
            row += step_row
            col += step_col
        
        #Regel: Zielfeld leer oder Gegner
        target_field = board[end_row][end_col]
        if target_field is None or target_field.color != self.color:
            return True
        
        return False