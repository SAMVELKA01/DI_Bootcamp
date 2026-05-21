# exercice 1
class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age


def find_oldest_cat(*cats):

    return max(cats, key=lambda cat: cat.age)


# Création des chats
cat1 = Cat("Minou", 3)
cat2 = Cat("Felix", 7)
cat3 = Cat("Garfield", 5)

# Recherche du plus âgé
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")

# exercice 2


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")


# Création des objets
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)

# Informations et méthodes
print(f"{davids_dog.name} mesure {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()

print(f"{sarahs_dog.name} mesure {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print()

# Comparaison des tailles
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est le plus grand chien.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} est le plus grand chien.")
else:
    print("Les deux chiens ont la même taille.")

# exercice 3


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Création de l'objet
stairway = Song(
    [
        "There’s a lady who's sure",
        "all that glitters is gold",
        "and she’s buying a stairway to heaven",
    ]
)

# Appel de la méthode
stairway.sing_me_a_song()

# exercice 4


class Zoo:

    def __init__(self, zoo_name):

        self.zoo_name = zoo_name
        self.animals = set()

    def add_animal(self, *new_animals):

        for animal in new_animals:
            self.animals.add(animal)

    def get_animals(self):

        print("Animaux du zoo :")

        for animal in sorted(self.animals):
            print(animal)

    def sell_animal(self, animal_sold):

        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")

    def sort_animals(self):

        grouped_animals = {}

        for animal in sorted(self.animals):
            first_letter = animal[0]

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        self.grouped_animals = grouped_animals

    def get_groups(self):

        for letter, animals in self.grouped_animals.items():
            print(f"{letter}: {animals}")


# Test
brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal(
    "Giraffe", "Bear", "Baboon", "Lion", "Zebra", "Cat", "Cougar"
)

brooklyn_safari.get_animals()

print()

brooklyn_safari.sell_animal("Bear")

print()

brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
