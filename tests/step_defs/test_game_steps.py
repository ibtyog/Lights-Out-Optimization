import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.data_module.board import Board
from src.game_module.game_engine import GameEngine
import copy

scenarios("../features/game_engine.feature")


@pytest.fixture
def context():
    return {}


@given("an empty board of size 5")
def empty_board(context):
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    context["board"] = Board(matrix)
    context["engine"] = GameEngine(context["board"])


@given(parsers.parse("a board solvable by clicking X: {x:d}, Y: {y:d}"))
def solvable_board(context, x, y):
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    board = Board(matrix)
    temp_engine = GameEngine(board)

    temp_engine.flip(x, y)

    context["board"] = Board(copy.deepcopy(temp_engine.board.matrix))
    context["engine"] = GameEngine(context["board"])


@when(parsers.parse("the engine flips the cell at X: {x:d}, Y: {y:d}"))
def flip_cell(context, x, y):
    context["engine"].flip(x, y)


@when(parsers.parse("the engine evaluates a solution that clicks X: {x:d}, Y: {y:d}"))
def eval_good_solution(context, x, y):
    solution = [[0 for _ in range(5)] for _ in range(5)]
    solution[y][x] = 1
    context["fitness"] = context["engine"].evaluate_solution(solution)


@when("the engine evaluates an empty solution")
def eval_empty_solution(context):
    solution = [[0 for _ in range(5)] for _ in range(5)]
    context["fitness"] = context["engine"].evaluate_solution(solution)


@then(parsers.parse("the cell at X: {x:d}, Y: {y:d} becomes {val:d}"))
def cell_becomes(context, x, y, val):
    assert context["board"].get_cell(x, y) == val


@then(parsers.parse("the cell at X: {x:d}, Y: {y:d} remains {val:d}"))
def cell_remains(context, x, y, val):
    assert context["board"].get_cell(x, y) == val


@then(parsers.parse("the objective function returns {val:d}"))
def check_objective(context, val):
    assert context["fitness"] == val
