# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_valid_word(self):
        new_game = Game()
        new_game.grid = ["A","B","R","Q","U","O","E","A","T"]
        self.assertEqual(new_game.is_valid("BAROQUE"), True)

    def test_invalid_word(self):
        new_game = Game()
        new_game.grid = ["A","B","R","Q","U","O","S","A","T"]
        self.assertEqual(new_game.is_valid("BAROQUE"), False)
