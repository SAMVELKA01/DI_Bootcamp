# exercice 1
print("Hello world\n" * 4)

# exercice 2

nombre = 99
puissance = nombre**3
resultat = puissance * 8
print(resultat)

# exercice 3

print(5 < 3)  # Prédiction : False
print(3 == 3)  # Prédiction : True
print(3 == "3")  # Prédiction : False
# print("3" > 3) # Prédiction : TypeError (Erreur car on ne peut pas comparer str et int)
print("Hello" == "hello")  # Prédiction : False

# exercice 4

computer_brand = "HP"
print("I have a " + computer_brand + " computer.")

# exercice 5

name = "samuel"
age = 19
shoe_size = 42
info = (
    "My name is "
    + name
    + ", I am "
    + str(age)
    + " years old and my shoe size is "
    + str(shoe_size)
    + "."
)
print(info)

# exercice 6

a = 12
b = 6
if a > b:
    print("Hello world")

# exercice 7

nombre = input("Entrez un nombre : ")
if int(nombre) % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

# exercice 8

mon_nom = "Samuel"
nom_utilisateur = input("Quel est ton nom ? ")

if nom_utilisateur.lower() == mon_nom.lower():
    print(f"Oh wow ! Tu t'appelles aussi {mon_nom} ? c'est cool ça !")
else:
    print(
        f"Enchanté {nom_utilisateur}, mais avoue que {mon_nom} ça claque quand même un peu plus, non ?"
    )

# exercice 9

taille = input("Quelle est votre taille en centimètres ? ")
taille_cm = int(taille)

if taille_cm > 145:
    print("Vous êtes assez grand pour monter à cheval !")
else:
    print("Vous devez encore grandir un peu pour pouvoir monter à cheval.")
