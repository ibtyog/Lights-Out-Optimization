import gurobipy as gp
from gurobipy import GRB
from typing import List
from src.data_module.board import Board
from .base_solver import BaseSolver


class GurobiSolver(BaseSolver):
    """Solver for the Lights Out puzzle using Gurobi optimization. Formulates the problem as an integer linear program."""

    def __init__(self, time_limit: int = 60, silent: bool = True):
        self.time_limit = time_limit
        self.silent = silent

    def solve(self, board: Board) -> List[List[int]]:
        size = board.size

        env = gp.Env(empty=True)
        if self.silent:
            env.setParam("OutputFlag", 0)
        env.start()

        model = gp.Model("LightsOut", env=env)
        model.setParam("TimeLimit", self.time_limit)

        x = {}
        for i in range(size):
            for j in range(size):
                x[i, j] = model.addVar(vtype=GRB.BINARY, name=f"x_{i}_{j}")

        k = {}
        for i in range(size):
            for j in range(size):
                k[i, j] = model.addVar(vtype=GRB.INTEGER, lb=0, name=f"k_{i}_{j}")

        model.setObjective(
            gp.quicksum(x[i, j] for i in range(size) for j in range(size)), GRB.MINIMIZE
        )

        directions = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(size):  # i to wiersz (Y)
            for j in range(size):  # j to kolumna (X)

                clicks_sum = gp.LinExpr()
                for dx, dy in directions:
                    nx, ny = j + dx, i + dy
                    if 0 <= nx < size and 0 <= ny < size:
                        clicks_sum += x[ny, nx]

                initial_state = board.get_cell(j, i)
                model.addConstr(
                    initial_state + clicks_sum == 2 * k[i, j], name=f"toggle_{i}_{j}"
                )

        model.optimize()

        if model.status in [GRB.OPTIMAL, GRB.TIME_LIMIT] and model.SolCount > 0:
            solution = [[0 for _ in range(size)] for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    if x[i, j].X > 0.5:
                        solution[i][j] = 1
            return solution
        else:
            raise ValueError(
                "Gurobi cannot find a solution within the time limit or the problem is infeasible."
            )
