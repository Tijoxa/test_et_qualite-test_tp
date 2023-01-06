import pytest
import mock

import TicTacToe_2016 as ttt

class TestZone:

    def testtrue(self):
        assert 1

    def test_create_grid(self):
        b = ttt.create_grid()
        print(b)
        assert b == [[" ", " ", " "],
                     [" ", " ", " "],
             [" ", " ", " "]]

    def test_sym():
        with mock.patch('builtins.input', return_value="X"):
            assert ttt.sym() == 'X', 'O'

        with mock.patch('builtins.input', return_value='O'):
            assert ttt.sym() == 'O', 'X'