import uuid

class User:
    def __init__(self, name, color):
        self.name = name  # Name des Spielers
        self.color = color  # 'white' oder 'black'
        self.id = str(uuid.uuid4())  # Eindeutige ID für den Spieler
        self.captured_pieces = []  # Liste der geschlagenen Figuren (UUIDs oder Objekte)
        self.move_history = []  # Historie der eigenen Züge

    def add_captured_piece(self, piece):
        """
        Fügt eine geschlagene Figur der Liste hinzu.
        """
        self.captured_pieces.append(piece)

    def record_move(self, move):
        """
        Fügt einen Zug zur Zughistorie hinzu.
        """
        self.move_history.append(move)

    def __str__(self):
        """
        Liefert eine String-Repräsentation des Spielers.
        """
        return f"Spieler {self.name} ({self.color})"

    def get_captured_pieces_summary(self):
        """
        Liefert eine Übersicht der geschlagenen Figuren.
        """
        return ", ".join(f"{piece.name} ({piece.color})" for piece in self.captured_pieces)
