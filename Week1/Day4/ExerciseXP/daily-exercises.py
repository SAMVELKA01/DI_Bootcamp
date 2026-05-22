# exercice 1
# Classe Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


# Classe Cat
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


# Classe Bengal
class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Classe Chartreux
class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Étape 1 : Classe Siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Étape 2 : Création des chats
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Milo", 5)
siamese_cat = Siamese("Luna", 2)

# Liste des chats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]


# Étape 3 : Instance de Pets
sara_pets = Pets(all_cats)


# Étape 4 : Promenade des chats
sara_pets.walk()

# exercice 2


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
            return f"{self.name} a gagné le combat contre {other_dog.name}"
        elif power_self < power_other:
            return f"{other_dog.name} a gagné le combat contre {self.name}"
        else:
            return f"{self.name} et {other_dog.name} sont à égalité"


# Étape 2 : Création des chiens
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Max", 3, 25)
dog3 = Dog("Rocky", 4, 18)

# Étape 3 : Tests des méthodes
print(dog1.bark())
print(dog2.bark())

print(f"Vitesse de {dog1.name} : {dog1.run_speed()}")
print(f"Vitesse de {dog2.name} : {dog2.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))

# L'exercice 3 est dans les fichiers Exercise3/dog.py et Exercise3/pet_dog.py


# exercice 4


class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:

                if member.is_18():
                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

                return

        print("Personne non trouvée.")

    def family_presentation(self):
        print(f"\nFamille {self.last_name}")
        print("-" * 30)

        for member in self.members:
            print(f"Nom : {member.first_name} {member.last_name}")
            print(f"Âge : {member.age}")
            print()


# Tests
my_family = Family("Kakou")

my_family.born("Samuel", 20)
my_family.born("Kevin", 15)
my_family.born("Sarah", 25)

my_family.check_majority("Samuel")
my_family.check_majority("Kevin")

my_family.family_presentation()
