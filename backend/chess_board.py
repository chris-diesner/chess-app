from backend.figures.pawn import Pawn
from backend.figures.rook import Rook
from backend.figures.knight import Knight
from backend.figures.bishop import Bishop
from backend.figures.queen import Queen
from backend.figures.king import King

class ChessBoard:
    def __init__(self):
        self.fields = [[None for _ in range(8)] for _ in range(8)]
        self.setup_fields()
        
    def notation_to_index(self, notation):
        columns = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        row = 8 - int(notation[1])  # Reihen 8-1 werden zu 0-7
        col = columns[notation[0].upper()]
        return row, col
        
    def setup_fields(self):
        #pawnn aufstellen
        for col in range(8):
            self.fields[6][col] = Pawn("white", (6, col))
            self.fields[1][col] = Pawn("black", (1, col))
            
        #uebrige Figuren aufstellen
        figures = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(8):
            self.fields[7][col] = figures[col]("white", (7, col))
            self.fields[0][col] = figures[col]("black", (0, col))
            
    def get_board_state(self):
        board_state = []
        for row in range(8):
            board_row = []
            for col in range(8):
                figure = self.fields[row][col]
                if figure:
                    board_row.append({
                        "type": figure.name,
                        "color": figure.color,
                        "position": f"{chr(97 + col)}{8 - row}"  
                    })
                else:
                    board_row.append(None)
            board_state.append(board_row)
        return board_state
            
    def print_board(self):
        print("    a  b  c  d  e  f  g  h")  # Spaltenkoordinaten
        print("  +------------------------+")
        for row in range(8):
            row_display = f"{8 - row} | "  # Zeilenkoordinate
            for col in range(8):
                piece = self.fields[row][col]
                # Figuren werden mit ihrem Kürzel dargestellt, leere Felder als □ oder ■
                if piece is None:  # Prüfe auf None, nicht auf " "
                    symbol = "□" if (row + col) % 2 == 0 else "■"
                else:
                    symbol = piece.__class__.__name__[0] if piece.color == "white" else piece.__class__.__name__[0].lower()
                row_display += f"{symbol}  "
            row_display += f"| {8 - row}"
            print(row_display)
        print("  +------------------------+")
        print("    a  b  c  d  e  f  g  h")