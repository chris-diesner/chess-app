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
            self.fields[0][i] = figures[i]              # weisse Figuren
            self.fields[7][i] = figures[i].lower()     # schwarze Figuren
            
    def print_board(self):
        for row in self.fields:
            print(" ".join(row))