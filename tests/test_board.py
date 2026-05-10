import pytest
from src.data_module.board import Board


def test_board_initialization():
    matrix = [[1, 0], [0, 1]]
    board = Board(matrix)

    assert board.size == 2
    assert board.get_cell(0, 0) == 1
    assert board.get_cell(1, 0) == 0


def test_board_set_cell_and_reset():
    matrix = [[0, 0], [0, 0]]
    board = Board(matrix)

    board.set_cell(0, 0, 1)
    assert board.get_cell(0, 0) == 1

    board.reset()
    assert board.get_cell(0, 0) == 0


def test_board_invalid_coordinates():
    matrix = [[0, 0], [0, 0]]
    board = Board(matrix)

    with pytest.raises(ValueError):
        board.get_cell(5, 5)
