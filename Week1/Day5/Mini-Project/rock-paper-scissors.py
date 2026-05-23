from game import Game


def get_user_menu_choice():

    print("\n=== MENU ===")
    print("(p) Jouer une nouvelle partie")
    print("(s) Afficher les scores")
    print("(q) Quitter")

    choice = input("Votre choix : ").lower().strip()

    while choice not in ["p", "s", "q"]:
        choice = input("Choix invalide. Réessayez : ").lower().strip()

    return choice


def print_results(results):

    print("\n=== RÉSULTATS ===")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Matchs nuls : {results['draw']}")

    print("\nMerci d'avoir joué !")


def main():

    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    while True:

        user_choice = get_user_menu_choice()

        if user_choice == "p":

            game = Game()

            result = game.play()

            results[result] += 1

        elif user_choice == "s":

            print_results(results)

        elif user_choice == "q":

            print_results(results)
            break


main()