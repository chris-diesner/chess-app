from chess_board import ChessBoard

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"
        
    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
    
    def move_figure(self, start_pos, end_pos):
        figure = self.board.fields[start_pos[0]][start_pos[1]]
        
        if figure is None:
            return "Hier steht keine Figur!"
        
        if figure.color != self.current_player:
            return f"Es ist {self.current_player}'s Zug!"
        
        if not figure.is_move_valid(start_pos, end_pos, self.board.fields):
            return "Ungültiger Zug!"
        
        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos
        
        self.switch_player()
        return "Guter Schachzug!"
    
    def print_board(self):
        print(f"Am Zug: {self.current_player}")
        self.board.print_board()