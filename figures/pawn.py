from figures.figure import Figure

class Pawn(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position, "Bauer")
        
    def is_move_valid(self, start_pos, end_pos, board):
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        #Regel: innerhalb Spielfeld
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False
        
        #Regel: weißer Bauer
        if self.color == "white":
            
            #Bauer ein Feld ziehen
            if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            #Bauer zwei Felder ziehen
            if start_row == 6 and end_row == start_row - 2 and start_col == end_col:
                if board[start_row - 1][start_col] is None and board[end_row][end_col] is None:
                    return True
                
            #Bauer diagonal schlagen
            if (
                end_row == start_row - 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                return True
            
        #Regel: schwarzer Bauer
        if self.color == "black":
            
            #Bauer ein Feld ziehen
            if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            #Bauer zwei Felder ziehen
            if start_row == 1 and end_row == start_row + 2 and start_col == end_col:
                if board[start_row + 1][start_col] is None and board[end_row][end_col] is None:
                    return True
                
            #Bauer diagonal schlagen
            if (
                end_row == start_row + 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                return True
        
        return False
