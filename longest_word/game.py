'''
TDD learning module
'''
import requests
import logging

class Game:
    ''' basic function to demonstrate TDD with'''

    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = list("OQUWRBAZE")
        self.word = ""

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        self.word = word
        # check if a word via LW dictionary API
        # https://dictionary.lewagon.com/:word
        url = f"https://dictionary.lewagon.com/{word}"
        response = requests.get(url=url)
        print(response.json())
        found = response.json()['found']
        if not found:
            return False
        # check in grid
        for c in self.word:
            if c not in self.grid:
                return False
        # second, check if ascii - maybe redundant
        if not ''.join(self.word).isascii():
            return False
        return True

if __name__ == "__main__":
    g = Game()
    print(g.is_valid("BOWER$"))
