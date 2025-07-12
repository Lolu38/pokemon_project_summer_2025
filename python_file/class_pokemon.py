class Pokemon:
    def __init__(self, name, level, type_):
        self.name = name
        self.level = level
        self.type_ = type_
        self.hp = level * 10
        self.attack = level * 2

    def __str__(self):
        return f"{self.name} (Level {self.level}, Type: {self.type_})"

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to Level {self.level}!")