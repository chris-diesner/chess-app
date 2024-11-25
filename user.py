import uuid

class User:
    def __init__(self, name, color):
        self.name = name
        self.color = color 
        self.id = str(uuid.uuid4())
        self.captured_figures = []
        self.move_history = []

    def add_captured_piece(self, piece):
        self.captured_pieces.append(piece)

    def record_move(self, move):
        self.move_history.append(move)

    def __str__(self):
        return f"Spieler {self.name} ({self.color})"

    def get_captured_pieces_summary(self):
        return ", ".join(f"{piece.name} ({piece.color})" for piece in self.captured_figures)