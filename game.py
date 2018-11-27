"""
Class Game
"""

import random
import string
import requests

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game:
    DICTIONARY_API = "https://wagon-dictionary.herokuapp.com/"
    def __init__(self):
        """
        Init class
        """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """
        :param word: the word to check
        :return: True if the word is valid, False either
        """
        if not word:
            return False
        for letter in word:
            try:
                self.grid.index(letter)
                self.grid.remove(letter)
            except ValueError:
                return False
        # Test if word is in dictionary
        r = requests.get(f"{self.DICTIONARY_API}{word}")
        if r.status_code != 200:
            return False
        resp = r.json()
        if not resp["found"]:
            return False
        return True


# if __name__ == "__main__":
#     new_game = Game()
#     new_game.grid = ["A", "B", "R", "Q", "U", "O", "E", "A", "T"]
#     print(new_game.is_valid("BAROQUE"))
