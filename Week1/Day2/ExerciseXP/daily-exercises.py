# exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

resultat = dict(zip(keys, values))

print(resultat)

# exercice 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = 0

for nom, age in family.items():

    if age < 3:
        prix = 0
    elif age <= 12:
        prix = 10
    else:
        prix = 15

    print(f"{nom} doit payer {prix}$")
    total += prix

print(f"Le coût total est de {total}$")

# exercice 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Modifier number_stores
brand["number_stores"] = 2

# Afficher une phrase
print(f"Zara crée des vêtements pour : {', '.join(brand['type_of_clothes'])}")

# Ajouter country_creation
brand["country_creation"] = "Spain"

# Ajouter Desigual aux concurrents
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Supprimer creation_date
brand.pop("creation_date")

# Afficher le dernier concurrent
print(brand["international_competitors"][-1])

# Afficher les couleurs aux USA
print(brand["major_color"]["US"])

# Afficher le nombre de clés
print(len(brand))

# Afficher toutes les clés
print(brand.keys())

# Bonus
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand)

# exercice 4

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# exercice 5

import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Appel de la fonction
compare_numbers(50)

# exercice 6

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# T-shirt large avec message par défaut
make_shirt()

# T-shirt medium avec message par défaut
make_shirt(size="medium")

# T-shirt personnalisé
make_shirt(size="small", text="Custom message")

# exercice 7

import random

# Fonction qui génère une température aléatoire
def get_random_temp():
    return round(random.uniform(-10, 40), 1)

# Fonction principale
def main():
    temperature = get_random_temp()

    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, it's freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temperature <= 23:
        print("Nice weather.")
    elif 24 <= temperature <= 32:
        print("It's a bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

# Appel de la fonction
main()

# exercice 8

toppings = []
price = 10

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping == "quit":
        break

    toppings.append(topping)
    price += 2.50

    print(f"Adding {topping} to your pizza.")

print("\nYour pizza toppings are:")
for topping in toppings:
    print(f"- {topping}")

print(f"Total price: ${price}")


