from figures.figure import Figure

class Pawn(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position, "Bauer")
        
    def is_move_valid(self, start_pos, end_pos, board, last_move=None):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if self.color == "white":
            #Regel: ein Feld nach vorne
            if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] is None:
                return True

            #Regel: zwei Felder nach vorne
            if start_row == 6 and end_row == start_row - 2 and start_col == end_col:
                if board[start_row - 1][start_col] is None and board[end_row][end_col] is None:
                    return True

            
            if end_row == start_row - 1 and abs(end_col - start_col) == 1:
                #Diagonaler Zug
                if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                    return True

                #En passant
                if last_move and isinstance(last_move["figure"], Pawn):
                    if (
                        last_move["start_pos"][0] == last_move["end_pos"][0] - 2 and  
                        last_move["end_pos"] == (start_row, end_col)
                    ):
                        return True

        if self.color == "black":
            #Regel: ein Feld nach vorne
            if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] is None:
                return True
            
            #Regel: zwei Felder nach vorne
            if start_row == 1 and end_row == start_row + 2 and start_col == end_col:
                if board[start_row + 1][start_col] is None and board[end_row][end_col] is None:
                    return True

            if end_row == start_row + 1 and abs(end_col - start_col) == 1:
                #Diagonaler Zug
                if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                    return True

                #En passant
                if last_move and isinstance(last_move["figure"], Pawn):
                    if (
                        last_move["start_pos"][0] == last_move["end_pos"][0] + 2 and  
                        last_move["end_pos"] == (start_row, end_col)
                    ):
                        return True

        return False
