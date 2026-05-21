class Voiture:
    marque = "Peugeot"

voiture_01 = Voiture()
voiture_02 = Voiture()
print(voiture_01.marque)
print(voiture_02.marque)

voiture_01.marque = "Renault"
print(voiture_01.marque)
print(voiture_02.marque)

voiture_01.marque = "bmw"
voiture_02.marque = "Mercedes"
print(Voiture.marque)
print(voiture_01.marque)
print(voiture_02.marque)