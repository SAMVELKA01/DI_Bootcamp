import random


class Game:
    def __init__(self):
        self.items = ["pierre", "feuille", "ciseaux"]

    def get_user_item(self):
        while True:
            user_choice = input(
                "Choisissez pierre, feuille ou ciseaux : "
            ).lower().strip()

            if user_choice in self.items:
                return user_choice

            print("Choix invalide. Réessayez.")

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"

        winning_cases = {
            "pierre": "ciseaux",
            "feuille": "pierre",
            "ciseaux": "feuille"
        }

        if winning_cases[user_item] == computer_item:
            return "win"

        return "loss"

    def play(self):

        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item)

        messages = {
            "win": "Vous avez gagné !",
            "loss": "Vous avez perdu !",
            "draw": "Match nul !"
        }

        print(
            f"\nVous avez choisi : {user_item}"
        )
        print(
            f"L'ordinateur a choisi : {computer_item}"
        )
        print(messages[result])

        return result