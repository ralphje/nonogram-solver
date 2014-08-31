import copy
from nonogram.puzzle import Puzzle

# Load the puzzle
puzzle = Puzzle([[6], [2, 2], [2, 2], [2, 5, 1], [1, 7, 1],
                 [1, 1, 3, 1], [3, 2, 1], [3, 1, 4], [3, 2, 4], [2, 2, 4],
                 [7, 3], [7, 3], [13], [5, 5], [1, 1, 3, 4],
                 [7, 5], [13], [5, 6], [4, 3, 4], [3, 3, 4],
                 [3, 2, 5], [1, 5, 4], [2, 6], [4, 3], [13],
                 [3, 4, 5], [1, 3, 1, 2], [1, 5, 1, 4], [1, 4, 1, 3], [1, 3, 1, 3],
                 [2, 4, 4], [9, 3], [4, 2, 3], [4, 2], [4]],
                [[3], [2], [9, 2],
                 [9, 6, 1], [4, 7, 6, 2], [1, 6, 4, 1, 2, 3, 2], [2, 12, 1, 2, 2, 2], [2, 4, 4, 2, 4, 5, 2],
                 [2, 1, 2, 3, 3, 5, 2, 3], [2, 2, 5, 3, 2, 1, 2, 6], [1, 2, 6, 1, 2, 5, 5], [1, 2, 2, 10, 1, 2], [1, 3, 3, 14, 2],
                 [1, 3, 16, 2, 1, 2], [2, 17, 2, 1, 1, 1], [2, 12, 1, 7], [2, 9], [3, 7]
                 ])

# The puzzle somehow consists of 18 rows, with the three rows on top, so we re-align the spacers
puzzle.spacer_offset_y = 3

# Empty print
puzzle.print()

# Step-by-step solver
while True:
    prev = copy.deepcopy(puzzle.board)
    input("")
    if not puzzle.solve_step():
        print("no next solution step")
    puzzle.print(prev)