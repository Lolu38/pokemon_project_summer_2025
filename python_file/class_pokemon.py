class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, type_,  attack_set, precision, esquive, img):
        self.name = name
        self.type_ = type_
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.attack_set = []
        self.precision = precision
        self.esquive = esquive
        self.img = img
        
    def __str__(self):
        return f"{self.name} (Type: {self.type_})"

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type_

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def get_attack_set(self):
        return self.attack_set
    
