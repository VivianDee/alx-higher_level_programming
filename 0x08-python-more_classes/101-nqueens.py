#!/usr/bin/python3
import sys
"""N Queens problem."""


class NQueens:
    """Class to solve the N Queens problem."""

    def __init__(self, size):
        """
        Initialize the NQueens instance.

        Args:
            size (int): The size of the chessboard and the number of queens.
        """
        self.__size = size
        self.__board = [['.' for _ in range(size)] for _ in range(size)]
        self.__solutions = []

    def solve(self):
        """Solve the N Queens problem and print the solutions."""
        self._solve_queens(0)
        self.print_solutions()

    def _solve_queens(self, col):
        """
        Recursive method to solve the N Queens problem.

        Args:
            col (int): The current column being processed.

        Returns:
            bool: True if a solution is found, False otherwise.
        """
        if col == self.__size:
            self.add_solution()
            return True

        for row in range(self.__size):
            if self._is_safe(row, col):
                self.__board[row][col] = (row, col)
                self._solve_queens(col + 1)
                self.__board[row][col] = '.'

    def _is_safe(self, row, col):
        """
        Check if it is safe to place a queen at the given position.

        Args:
            row (int): The row index of the position.
            col (int): The column index of the position.

        Returns:
            bool: True if it is safe to place a queen, False otherwise.
        """
        for i in range(col):
            if self.__board[row][i] == (row, i):
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.__board[i][j] == (i, j):
                return False

        for i, j in zip(range(row, self.__size), range(col, -1, -1)):
            if self.__board[i][j] == (i, j):
                return False

        return True

    def add_solution(self):
        """Add a solution to the list of solutions."""
        solution = []
        for row in self.__board:
            queens = [cell for cell in row if isinstance(cell, tuple)]
            solution.append(queens)
        self.__solutions.append(solution)

    def print_solutions(self):
        """Print the solutions."""
        self.__solutions.reverse()
        for solution in self.__solutions:
            print("[", end="")
            for row in solution:
                for i, j in row:
                    print(f"[{i}, {j}]",  end="")
                    if solution.index(row) < len(solution) - 1:
                        print(", ", end="")
            print("]")


def nqueens(size):
    """
    Solve the N Queens problem and print the solutions.

    Args:
        size (int): The size of the chessboard and the number of queens.
    """
    if not isinstance(size, int):
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    queens = NQueens(size)
    queens.solve()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
        nqueens(size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
