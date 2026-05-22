from dog import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dogs)} jouent tous ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            print(f"{self.name} {random.choice(tricks)}")


# Tests
dog1 = PetDog("Rex", 4, 20)
dog2 = PetDog("Max", 3, 18)
dog3 = PetDog("Rocky", 5, 25)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()