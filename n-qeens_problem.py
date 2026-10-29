# 5. Advanced — Solve the N-Queens Problem
# Hard
# Suggested time: 45–90 minutes

# Problem

# Write a function solve_n_queens(n) that finds all valid arrangements of n queens on an \(n \times n\) chessboard.

# The queens must be placed so that no two queens attack each other.

# Queens can attack along:
# - The same row.
# - The same column.
# - Either diagonal.
# For n = 4, there are two valid arrangements.

# Requirements
# - Use recursion and backtracking.
# - Return all valid arrangements.
# - Represent each arrangement as a list of strings, using "Q" for a queen and "." for an empty square.
# - Do not use external libraries.
# Hint: Place one queen in a row at a time. For each column, check whether placing a queen there is safe. If it is, continue to the next row. If you reach a dead end, undo the last placement and try another column.
