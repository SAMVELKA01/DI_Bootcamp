# Challenge 1

word = input("Enter a word: ")

letter_index = {}

for index, letter in enumerate(word):

    if letter in letter_index:
        letter_index[letter].append(index)
    else:
        letter_index[letter] = [index]

print(letter_index)

# Challenge 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"

# Nettoyer le portefeuille
money = int(wallet.replace("$", "").replace(",", ""))

basket = []

# Parcourir les articles
for item, price in items_purchase.items():

    # Nettoyer le prix
    clean_price = int(price.replace("$", "").replace(",", ""))

    # Vérifier si l'article est abordable
    if clean_price <= money:
        basket.append(item)
        money -= clean_price

# Affichage du résultat
if len(basket) == 0:
    print("Nothing")
else:
    print(sorted(basket))
