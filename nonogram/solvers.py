
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve_step(self):
        raise NotImplementedError()


class SimpleSolver(Solver):
    pos = 0
    working_on = "x"

    def solve_step(self):
        cpos = self.pos
        cworking_on = self.working_on

        # Loop over all possible lines until we have done something or we have gone a full round without doing anything
        done_anything = self._solve_step(self.pos, self.working_on)
        while not done_anything:
            self._next_step()
            if self.pos == cpos and self.working_on == cworking_on:
                return False
            done_anything = self._solve_step(self.pos, self.working_on)
        self._next_step()
        return True

    def _next_step(self):
        """Increase the internal position counters by 1"""

        if self.working_on == "x" and self.pos >= len(self.puzzle.horizontals) - 1:
            self.working_on = "y"
            self.pos = 0
        elif self.working_on == "y" and self.pos >= len(self.puzzle.verticals) - 1:
            self.working_on = "x"
            self.pos = 0
        else:
            self.pos += 1

    def _solve_step(self, pos, solve):
        """Solve a single step, returns whether something has changed."""

        if solve == "x":
            result = SimpleSolver._solve_line(self.puzzle.board[pos].copy(), self.puzzle.horizontals[pos])
            did_anything = self.puzzle.board[pos] != result
            self.puzzle.board[pos] = result
        else:
            result = SimpleSolver._solve_line([c[pos] for c in self.puzzle.board], self.puzzle.verticals[pos])
            did_anything = False
            for i, r in enumerate(result):
                did_anything = did_anything or r != self.puzzle.board[i][pos]
                self.puzzle.board[i][pos] = r
        return did_anything

    @staticmethod
    def _solve_line(current_line, specs):
        """"Solves a single line (horizontal or vertical) according to the spec."""

        permutations = SimpleSolver._permutations(current_line, specs)
        columns = zip(*permutations)
        for i, states in enumerate(columns):
            if all(states):
                current_line[i] = True
            elif all((l is False for l in states)):
                current_line[i] = False
        return current_line

    @staticmethod
    def _permutations(line, specs):
        """Yields all possible permutations of the given line given the specs"""

        # When there are no specs, everything in the line must be empty
        if not specs:
            yield [False] * len(line)
            return

        block, other_blocks = specs[0], specs[1:]

        # Get all possible permutations of space before the first block
        space_needed_for_other_blocks = len(other_blocks) + sum(other_blocks)
        for space in range(len(line) - space_needed_for_other_blocks - block + 1):
            # Check if this amount of space is valid:
            # - not any of the places before this block is currently set
            # - none of the spaces covered by this block must be unset
            # - the space after this block must not be set
            # - there must not be any remaining set blocks if this is the last block
            if any(line[0:space]) or \
                    any((l is False for l in line[space:space + block])) or \
                    (len(line) > (space + block) and line[space + block]) or \
                    not other_blocks and any(line[space + block:]):
                continue

            # Recurse by chopping off the block according to our new specs and attempt to do something
            for permutation in SimpleSolver._permutations(line[space + block + 1:], other_blocks):
                l2 = line.copy()
                l2[:space] = [False] * space  # space of length space
                l2[space:space + block] = [True] * block  # then true of length block
                if len(line) > space + block:
                    l2[space + block] = False  # then a false block if needed
                l2[space + block + 1:] = permutation  # then the rest
                yield l2