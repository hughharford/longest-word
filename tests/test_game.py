# tests/test_game.py

from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
        g = Game()
            # exercise
        grid = g.grid
            # verify
        assert isinstance(grid, list) # test type
        assert len(grid) == 9 # test length
        assert ''.join(grid).isascii() # test all ascii characters
            # teardown

    def test_grid_validity(self):
        g = Game()
        # test valid word checks out correct
        GRID = "OQUWRBAZE" ' the default'
        valid_word = "BAROQUE"
        assert g.is_valid(valid_word)
        # test invalid word 1 checks out wrong
        invalid_word_1 = "BAROQUEY"
        assert not g.is_valid(invalid_word_1)
        # test invalid word 2 checks out wrong
        invalid_word_2 = "9988776655"
        assert not g.is_valid(invalid_word_2)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
