def print_board(board, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def solve_n_queens(n):
    board = [-1] * n  # board[i] = column position of queen in row i
    col_used = [False] * n
    left_diag = [False] * (2 * n - 1)  # row + col
    right_diag = [False] * (2 * n - 1)  # row - col + n - 1

    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if not col_used[col] and not left_diag[row + col] and not right_diag[row - col + n - 1]:
                # Place the queen
                board[row] = col
                col_used[col] = left_diag[row + col] = right_diag[row - col + n - 1] = True

                backtrack(row + 1)

                # Remove the queen (backtrack)
                col_used[col] = left_diag[row + col] = right_diag[row - col + n - 1] = False
                board[row] = -1

    backtrack(0)

    return solutions

# Main
if __name__ == "__main__":
    n = int(input("Enter the value of N (number of queens): "))
    solutions = solve_n_queens(n)

    print(f"\nTotal solutions for {n}-Queens: {len(solutions)}")
    for index, solution in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        print_board(solution, n)
