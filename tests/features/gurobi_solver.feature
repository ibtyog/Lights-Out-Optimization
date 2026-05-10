Feature: Gurobi Exact Solver
  Researcher
  wants to use Gurobi to find the mathematically optimal solution
  So that he has a baseline for evaluating metaheuristics

  Scenario: Gurobi finds the optimal solution for a solvable board
    Given a board solvable by clicking X: 2, Y: 2
    When Gurobi solver processes the board
    Then the solver returns a valid solution matrix
    And the solution requires exactly 1 click