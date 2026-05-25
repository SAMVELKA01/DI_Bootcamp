# Exercice 1

# Introduction à l’analyse des données

# L’analyse des données est le processus qui consiste à collecter, organiser, nettoyer, examiner et interpréter des données afin d’en tirer des informations utiles. Elle permet de transformer des données brutes en connaissances exploitables pour aider à la prise de décision. Grâce aux outils modernes comme Python, Pandas ou encore les logiciels de visualisation, l’analyse des données est devenue un élément essentiel dans presque tous les domaines professionnels.

# Aujourd’hui, l’analyse des données joue un rôle très important dans les contextes modernes. Les entreprises, les gouvernements et les organisations produisent chaque jour une énorme quantité de données. Sans analyse, ces informations n’auraient aucune utilité. L’analyse des données permet d’identifier des tendances, de prévoir des comportements futurs, d’améliorer les performances et de prendre des décisions plus précises et rapides. Elle contribue également à réduire les coûts, optimiser les stratégies et améliorer l’expérience des utilisateurs ou des clients.

# L’un des principaux domaines d’application de l’analyse des données est le secteur de la santé. Les hôpitaux et les chercheurs utilisent les données pour suivre les maladies, améliorer les traitements et détecter plus rapidement certains problèmes médicaux. Pendant les épidémies, l’analyse des données aide aussi à prévoir la propagation des maladies et à organiser les réponses sanitaires.

# Le commerce et le marketing représentent un autre domaine important. Les entreprises analysent les habitudes d’achat des clients afin de proposer des recommandations personnalisées, améliorer leurs produits et cibler efficacement leurs campagnes publicitaires. Des plateformes comme Amazon ou Netflix utilisent fortement l’analyse des données pour recommander des produits ou des contenus adaptés aux utilisateurs.

# Enfin, l’analyse des données est également très utilisée dans le domaine financier. Les banques et les entreprises financières analysent les données pour détecter les fraudes, évaluer les risques et prévoir les tendances économiques. Les investisseurs utilisent aussi les données pour prendre de meilleures décisions sur les marchés financiers.

# En conclusion, l’analyse des données est devenue indispensable dans le monde moderne. Elle aide les organisations à comprendre les informations disponibles, à résoudre des problèmes complexes et à prendre des décisions plus intelligentes. Avec l’évolution de la technologie et de l’intelligence artificielle, son importance continuera de grandir dans les années à venir.



# Exercice 2
import pandas as pd


# =========================
# DATASET 1 : SLEEP
# =========================

sleep_df = pd.read_csv("datasets/sleep.csv")

print("\n===== DATASET SOMMEIL =====")
print(sleep_df.head())

print("\nDescription :")
print(
    "Ce dataset contient des informations sur "
    "les habitudes de sommeil des Américains."
)


# =========================
# DATASET 2 : MENTAL HEALTH
# =========================

mental_df = pd.read_csv("datasets/mental_health.csv")

print("\n===== DATASET SANTÉ MENTALE =====")
print(mental_df.head())

print("\nDescription :")
print(
    "Ce dataset contient des statistiques "
    "mondiales sur les troubles mentaux."
)


# =========================
# DATASET 3 : CREDIT CARD
# =========================

credit_df = pd.read_csv("datasets/credit_card.csv")

print("\n===== DATASET CARTES DE CRÉDIT =====")
print(credit_df.head())

print("\nDescription :")
print(
    "Ce dataset contient des informations "
    "sur les approbations de cartes de crédit."
)


# Exercice 3

import pandas as pd

sleep_df = pd.read_csv("datasets/sleep.csv")

print(sleep_df.info())

print("""

===== ANALYSE =====

Year :
Quantitatif
→ Valeur numérique représentant une année.

Period :
Qualitatif
→ Catégorie descriptive.

Avg hrs per day sleeping :
Quantitatif
→ Mesure numérique du sommeil.

""")


# Exercice 4

import pandas as pd


# Charger le dataset Iris
iris_df = pd.read_csv("datasets/iris.csv")


# Afficher les premières lignes
print("\n===== DATASET IRIS =====")
print(iris_df.head())


# Informations générales
print("\n===== INFORMATIONS =====")
print(iris_df.info())


# Analyse des types de données
print("""

===== ANALYSE DES COLONNES =====


sepal_length
Quantitatif
→ représente une mesure numérique de longueur.


sepal_width
Quantitatif
→ représente une mesure numérique de largeur.


petal_length
Quantitatif
→ représente une mesure numérique de longueur.


petal_width
Quantitatif
→ représente une mesure numérique de largeur.


species
Qualitatif
→ représente une catégorie de fleur
(Setosa, Versicolor, Virginica).

""")

# Exercice 5

import pandas as pd


# Charger le dataset
sleep_df = pd.read_csv("datasets/sleep.csv")


# Afficher les premières lignes
print("\n===== DATASET SOMMEIL =====")
print(sleep_df.head())


# Informations sur le dataset
print("\n===== INFORMATIONS =====")
print(sleep_df.info())


# Analyse des colonnes
print("""

===== OBSERVATION ET ANALYSE =====


1. Year
Type d’analyse :
→ Analyse de tendances

Pourquoi ?
→ Cette colonne représente les années.
Elle permet d’observer l’évolution du sommeil
des Américains dans le temps.


2. Period
Type d’analyse :
→ Comparaison de groupes

Pourquoi ?
→ Cette colonne représente des catégories
ou périodes différentes qui peuvent être comparées.


3. Avg hrs per day sleeping
Type d’analyse :
→ Analyse statistique et tendances

Pourquoi ?
→ Cette colonne contient le nombre moyen
d’heures de sommeil.
Elle permet de calculer des moyennes,
identifier des variations et observer des tendances.

""")

# Exercice 6

# Les rapports financiers d'une entreprise stockés dans un fichier Excel
# → Données structurées
# Car les données sont organisées en lignes et colonnes avec un format précis.
# Photographies téléchargées sur une plateforme de médias sociaux
# → Données non structurées
# Car les images ne sont pas organisées dans un format tabulaire.
# Une collection d'articles de presse sur un site web
# → Données non structurées
# Car les articles sont principalement du texte libre.
# Données d'inventaire dans une base de données relationnelle
# → Données structurées
# Car elles sont stockées dans des tables organisées avec des colonnes définies.
# Enregistrements d'entretiens issus d'une étude de marché
# → Données non structurées
# Car les fichiers audio ou les conversations ne suivent pas une structure tabulaire fixe.


# Exercice 7

# Une série d’articles de blog sur les expériences de voyage
# → Méthode : Traitement du langage naturel (NLP)

# Les articles peuvent être analysés pour extraire des informations importantes comme :

# le lieu
# la date
# les sentiments
# les activités mentionnées

# Ces informations peuvent ensuite être stockées dans un tableau ou une base de données.

# Justification :
# Le NLP permet de transformer du texte libre en données organisées et exploitables.

# Enregistrements audio des appels au service client
# → Méthode : Transcription vocale automatique

# Les fichiers audio peuvent être convertis en texte grâce à la reconnaissance vocale, puis les informations importantes peuvent être classées dans des colonnes.

# Exemples :

# nom du client
# type de problème
# durée de l’appel

# Justification :
# La conversion audio → texte facilite l’analyse et l’organisation des données.

# Notes manuscrites issues d’une séance de brainstorming
# → Méthode : OCR (Reconnaissance optique de caractères)

# Les notes manuscrites peuvent être numérisées puis converties en texte grâce à un logiciel OCR.

# Les idées peuvent ensuite être classées par catégories dans un tableau.

# Justification :
# L’OCR transforme des documents manuscrits en données textuelles structurées.

# Un tutoriel vidéo sur la cuisine
# → Méthode : Extraction de texte et segmentation vidéo

# La vidéo peut être transcrite en texte puis les informations importantes peuvent être organisées :

# ingrédients
# étapes
# durée
# type de recette

# Justification :
# La transcription et l’extraction d’informations permettent de convertir une vidéo non structurée en données facilement analysables.


# Exercice 8

import pandas as pd


# Charger le dataset
train_df = pd.read_csv("datasets/train.csv")


# Afficher les premières lignes
print("\n===== PREMIÈRES LIGNES DU DATASET =====")
print(train_df.head())

# Exercice 9

import pandas as pd


# Création du dataframe
data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Ville": ["Paris", "Londres", "Abidjan"]
}

df = pd.DataFrame(data)


# Affichage du dataframe
print("\n===== DATAFRAME =====")
print(df)


# Export Excel
df.to_excel(
    "exports/dataframe.xlsx",
    index=False
)

print("\nFichier Excel exporté avec succès.")


# Export JSON
df.to_json(
    "exports/dataframe.json",
    orient="records",
    indent=4
)

print("Fichier JSON exporté avec succès.")


# Exercice 10

import pandas as pd


# URL du dataset JSON
url = "https://jsonplaceholder.typicode.com/posts"


# Lire les données JSON
df = pd.read_json(url)


# Afficher les 5 premières lignes
print("\n===== PREMIÈRES LIGNES =====")
print(df.head())