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
        # test type
        assert isinstance(grid, list)
        # test length
        assert len(grid) == 9
        # test all ascii characters
        assert ''.join(grid).isascii()
            # teardown

    def test_grid_validity(self):
        g = Game()
        # test valid word checks out correct
        GRID = "OQUWRBAZE"

        valid_word = "BAROQUE"
        assert g.is_valid(valid_word)
        # test invalid word 1 checks out wrong
        invalid_word_1 = "BAROQUEY"
        assert not g.is_valid(invalid_word_1)
        # test invalid word 2 checks out wrong
        invalid_word_2 = "9988776655"
        assert not g.is_valid(invalid_word_2)
