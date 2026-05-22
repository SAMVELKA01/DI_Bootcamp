class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        power_self = self.run_speed() * self.weight
        power_other = other_dog.run_speed() * other_dog.weight

        if power_self > power_other:
            return f"{self.name} a gagné le combat"
        elif power_self < power_other:
            return f"{other_dog.name} a gagné le combat"

        return "Égalité"