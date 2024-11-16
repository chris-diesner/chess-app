class ChessBoard:
    def __init__(self):
        self.fields = [[" " for _ in range(8)] for _ in range(8)]
        self.setup_fields()
        
    def setup_fields(self):
        #Figuren Setup - Weisse Figuren = Grossbuchstaben, Schwarze Figuren = Kleinbuchstaben
        #hier werden die Bauern aufgestellt
        for i in range(8):
            self.fields[1][i] = "P"
            self.fields[6][i] = "p"
        
        #hier werden die uebrigen Figuren aufgestellt
        figures = ["R", "N", "B", "Q", "K", "B", "N", "R"]  
        for i in range(8):
            self.fields[0][i] = figures[i]              
            self.fields[7][i] = figures[i].lower()     
            
    def print_board(self):
        print("    a  b  c  d  e  f  g  h")  # Spaltenkoordinaten
        print("  +------------------------+")
        for row in range(8):
            row_display = f"{8 - row} | "  # Zeilenkoordinate
            for col in range(8):
                piece = self.fields[row][col] if self.fields[row][col] != " " else "□" if (row + col) % 2 == 0 else "■"
                row_display += f"{piece}  "
            row_display += f"| {8 - row}"
            print(row_display)
        print("  +------------------------+")
        print("    a  b  c  d  e  f  g  h")
