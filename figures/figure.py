import uuid

class Figure:
    
    def __init__(self, color, position, name):
        self.color = color
        self.position = position
        self.name = name
        self.id = str(uuid.uuid4())