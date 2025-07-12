class Pokemon:
    def __init__(self, name, level, type_):
        self.name = name
        self.type_ = type_
        self.hp = level * 10
        self.attack = level * 2
        self.defense = level * 2
        self.speed = level * 2
        self.attacks = []
        
    def __str__(self):
        return f"{self.name} (Type: {self.type_})"


