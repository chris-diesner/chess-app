from figures.figure import Figure

class Rook(Figure):
    
    def is_move_valid(self, start_pos, end_pos, board):
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        #Regel: Turm bewegt sich nur horizontal oder vertikal
        if start_row != end_row and start_col != end_col:
            return False
        
        #Regel: Turm darf keine Figuren ueberspringen
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range (start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
                
        elif start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range (start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
        
        #Regel: Zielfeld leer oder Gegner
        target_field = board[end_row][end_col]
        if target_field is None or target_field.color != self.color:
            return True
        
        return False