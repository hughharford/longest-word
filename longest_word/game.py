'''
TDD learning module
'''
class Game:
    ''' basic function to demonstrate TDD with'''
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = list("OQUWRBAZE")
        self.word = ""
    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        self.word = word
        for c in self.word:
            if c not in self.grid:
                return False
        if not ''.join(self.word).isascii():
            return False
        return True
