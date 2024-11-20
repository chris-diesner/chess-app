from chess_board import ChessBoard

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"
        
    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
        
    def convert_to_coordinates(self, pos):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        row = 8 - pos[0]
        column = columns[pos[1]]
        return f"{column}{row}"
    
    def move_figure(self, start_pos, end_pos):
        figure = self.board.fields[start_pos[0]][start_pos[1]]
        target_field = self.board.fields[end_pos[0]][end_pos[1]]
        
        if figure is None:
            return "Du hast ein leeres Feld ausgewählt!"
        
        if figure.color != self.current_player:
            return f"Es ist {self.current_player}'s Zug!"
        
        if not figure.is_move_valid(start_pos, end_pos, self.board.fields):
            return "Ungültiger Zug!"
        
        if target_field is None:
            move_notation = f"{figure.name} ({'weiß' if figure.color == 'white' else 'schwarz'}) von {self.convert_to_coordinates(start_pos)} auf {self.convert_to_coordinates(end_pos)}"
        else:
            move_notation = f"{figure.name} ({'weiß' if figure.color == 'white' else 'schwarz'}) schlägt {target_field.name} ({'weiß' if target_field.color == 'white' else 'schwarz'}) von {self.convert_to_coordinates(start_pos)} auf {self.convert_to_coordinates(end_pos)}"
        
        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos
        
        self.switch_player()
        self.print_board()
        return move_notation
    
    def print_board(self):
        print(f"Am Zug: {self.current_player}")
        self.board.print_board()