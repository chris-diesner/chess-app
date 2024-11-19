from figures.figure import Figure

class Pawn(Figure):
    def is_move_valid(self, start_pos, end_pos, board):
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        #Regel: weisser Bauer
        if self.color == "white":
            
            #Bauer nur ein Feld vorwaerts
            if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            #Bauer zwei Felder vorwaerts wenn er noch nicht bewegt wurde
            if start_row == 1 and end_row == start_row + 2 and start_col == end_col:
                if board[start_row + 1][start_col] is None and board[end_row][end_col] is None:
                    return True
                
            #Bauer schlaegt diagonal
            if (
                end_row == start_row + 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                return True
            
        #Regel: schwarzer Bauer
        if self.color == "black":
            
            #Bauer nur ein Feld vorwaerts
            if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            #Bauer zwei Felder vorwaerts wenn er noch nicht bewegt wurde
            if start_row == 6 and end_row == start_row - 2 and start_col == end_col:
                if board[start_row - 1][start_col] is None and board[end_row][end_col] is None:
                    return True
                
            #Bauer schlaegt diagonal
            if (
                end_row == start_row - 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                return True