from figures.figure import Figure

class Pawn(Figure):
    
    def __init__(self, color, position):
        super().__init__(color, position, "Bauer")
        
    def is_move_valid(self, start_pos, end_pos, board):
        print(f"DEBUG: Prüfe Zug von {start_pos} nach {end_pos} für {self.color} Bauer.")
        
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # Regel: Züge nur innerhalb Spielfeld
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print("DEBUG: Ziel außerhalb des Spielfelds!")
            return False
        
        # Regel: weißer Bauer
        if self.color == "white":
            print("DEBUG: Weißer Bauer - Zugregel wird geprüft.")
            
            # Bauer nur ein Feld vorwärts
            if end_row == start_row - 1 and start_col == end_col and board[end_row][end_col] is None:
                print("DEBUG: Einfacher Vorwärtszug erfolgreich!")
                return True
            
            # Bauer zwei Felder vorwärts, wenn er noch nicht bewegt wurde
            if start_row == 6 and end_row == start_row - 2 and start_col == end_col:
                if board[start_row - 1][start_col] is None and board[end_row][end_col] is None:
                    print("DEBUG: Doppelschritt erfolgreich!")
                    return True
                
            # Bauer schlägt diagonal
            if (
                end_row == start_row - 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                print("DEBUG: Schlagzug erfolgreich!")
                return True
            
        # Regel: schwarzer Bauer
        if self.color == "black":
            print("DEBUG: Schwarzer Bauer - Zugregel wird geprüft.")
            
            # Bauer nur ein Feld vorwärts
            if end_row == start_row + 1 and start_col == end_col and board[end_row][end_col] is None:
                print("DEBUG: Einfacher Vorwärtszug erfolgreich!")
                return True
            
            # Bauer zwei Felder vorwärts, wenn er noch nicht bewegt wurde
            if start_row == 1 and end_row == start_row + 2 and start_col == end_col:
                if board[start_row + 1][start_col] is None and board[end_row][end_col] is None:
                    print("DEBUG: Doppelschritt erfolgreich!")
                    return True
                
            # Bauer schlägt diagonal
            if (
                end_row == start_row + 1 and
                abs(end_col - start_col) == 1 and
                board[end_row][end_col] is not None and
                board[end_row][end_col].color != self.color
            ):
                print("DEBUG: Schlagzug erfolgreich!")
                return True
        
        print("DEBUG: Keine gültige Zugregel erfüllt.")
        return False
