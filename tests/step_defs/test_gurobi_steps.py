import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.data_module.board import Board
from src.game_module.game_engine import GameEngine
from src.algorithms_module.gurobi_solver import GurobiSolver
import copy

scenarios("../features/gurobi_solver.feature")


@pytest.fixture
def context():
    """Słownik do przekazywania stanu między krokami testu."""
    return {}


@given(parsers.parse("a board solvable by clicking X: {x:d}, Y: {y:d}"))
def solvable_board(context, x, y):
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    board = Board(matrix)
    temp_engine = GameEngine(board)
    temp_engine.flip(x, y)

    context["board"] = Board(copy.deepcopy(temp_engine.board.matrix))


@when("Gurobi solver processes the board")
def run_gurobi(context):
    solver = GurobiSolver(silent=True)
    context["solution"] = solver.solve(context["board"])


@then("the solver returns a valid solution matrix")
def check_valid_matrix(context):
    assert context["solution"] is not None
    assert len(context["solution"]) == 5
    assert len(context["solution"][0]) == 5


@then(parsers.parse("the solution requires exactly {clicks:d} click"))
def check_clicks(context, clicks):
    total_clicks = sum(sum(row) for row in context["solution"])
    assert total_clicks == clicks
