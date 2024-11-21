from chess_board import ChessBoard
from figures.king import King

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"
        
    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"
        if self.check_stalemate():
            print("Patt!")
        
    def check_stalemate(self):
        stalemate = self.is_stalemate(self.current_player)
        if stalemate:
            return True
        return False
        
    def convert_to_coordinates(self, pos):
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        row = 8 - pos[0]
        column = columns[pos[1]]
        return f"{column}{row}"
    
    def is_king_in_check(self, current_player):
        king_pos = None
        attacking_figures = []
        for row in range(8):
            for col in range(8): 
                figure = self.board.fields[row][col]
                if figure and isinstance(figure, King) and figure.color == current_player:
                    king_pos = (row, col)
                    break
                
        for row in range(8):
            for col in range(8): 
                figure = self.board.fields[row][col]
                if figure and figure.color != current_player:
                    if figure.is_move_valid((row, col), king_pos, self.board.fields):
                        attacking_figures.append((figure, (row, col)))
        return len(attacking_figures) > 0, attacking_figures
    
    def is_king_in_checkmate(self, current_player):
        king_in_check, attacking_figures = self.is_king_in_check(current_player)
        if not king_in_check:
            return False
        
        #kann angreifende Figur geschlagen werden
        if len(attacking_figures) == 1:
            attacker_pos = attacking_figures[0][1]
            for row in range(8):
                for col in range(8):
                    figure = self.board.fields[row][col]
                    if figure and figure.color == current_player:
                        if figure.is_move_valid((row, col), attacker_pos, self.board.fields):
                            if not self.simulate_move_and_check(current_player, (row, col), attacker_pos):
                                return False

        #kann König ausweichen
        king_pos = None
        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if isinstance(figure, King) and figure.color == current_player:
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        king = self.board.fields[king_pos[0]][king_pos[1]]
        for end_row in range(8):
            for end_col in range(8):
                if king.is_move_valid(king_pos, (end_row, end_col), self.board.fields):
                    if not self.simulate_move_and_check(current_player, king_pos, (end_row, end_col)):
                        return False
                    
        #kann angreifende Figur blockiert werden
        if len(attacking_figures) == 1:
            attacker_pos = attacking_figures[0][1]
            blocking_positions = self.get_positions_between(king_pos, attacker_pos)
            
            for row in range(8):
                for col in range(8):
                    figure = self.board.fields[row][col]
                    if figure and figure.color == current_player:
                        for block_pos in blocking_positions:
                            if figure.is_move_valid((row, col), block_pos, self.board.fields):
                                if not self.simulate_move_and_check(current_player, (row, col), block_pos):
                                    return False
        return True
        
    #Methode zum Simulieren eines Zuges
    def simulate_move_and_check(self, current_player, start_pos, end_pos):
        temp_field = self.board.fields[end_pos[0]][end_pos[1]]
        figure = self.board.fields[start_pos[0]][start_pos[1]]

        self.board.fields[end_pos[0]][end_pos[1]] = figure
        self.board.fields[start_pos[0]][start_pos[1]] = None
        figure.position = end_pos

        still_in_check = self.is_king_in_check(current_player)[0]

        self.board.fields[start_pos[0]][start_pos[1]] = figure
        self.board.fields[end_pos[0]][end_pos[1]] = temp_field
        figure.position = start_pos

        return still_in_check
    
    #Hilfsmethode um Felder zum Blockieren zu finden
    def get_positions_between(self, start_pos, end_pos):
        positions = []
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                positions.append((start_row, col))
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                positions.append((row, start_col))
        elif abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if start_row < end_row else -1
            col_step = 1 if start_col < end_col else -1
            for i in range(1, abs(start_row - end_row)):
                positions.append((start_row + i * row_step, start_col + i * col_step))
        return positions
    
    #Methode prueft auf Patt
    def is_stalemate(self, current_player):
        king_in_check, _ = self.is_king_in_check(current_player)
        if king_in_check:
            return False
        
        for row in range(8):
            for col in range(8):
                figure = self.board.fields[row][col]
                if figure and figure.color == current_player:
                    start_pos = (row, col)
                    for end_row in range(8):
                        for end_col in range(8):
                            end_pos = (end_row, end_col)
                            if figure.is_move_valid(start_pos, end_pos, self.board.fields):
                                if not self.simulate_move_and_check(current_player, start_pos, end_pos):
                                    return False
        return True


    def move_figure(self, start_pos, end_pos):
        figure = self.board.fields[start_pos[0]][start_pos[1]]
        target_field = self.board.fields[end_pos[0]][end_pos[1]]
        
        if figure is None:
            return "Du hast ein leeres Feld ausgewählt!"
        
        if figure.color != self.current_player:
            return f"Es ist {self.current_player}'s Zug!"
        
        if not figure.is_move_valid(start_pos, end_pos, self.board.fields):
            return "Ungültiger Zug!"
        
        if self.simulate_move_and_check(self.current_player, start_pos, end_pos):
            return "ungültiger Zug! König im Schach!"
        
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