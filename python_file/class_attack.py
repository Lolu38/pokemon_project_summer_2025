class Attack:
    def __init__(self, name, power, type_, nbr_uses):
        self.name = name
        self.power = power
        self.type_ = type_
        self.nbr_uses = nbr_uses

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Type: {self.type_})"

    def get_power(self):
        return self.power
    
    def get_type(self):
        return self.type_

    def get_name(self):
        return self.name

    def get_nbr_uses(self):
        return self.nbr_uses