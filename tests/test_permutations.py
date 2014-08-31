import unittest
from nonogram.solvers import SimpleSolver


class SolutionTest(unittest.TestCase):

    def test_simple_boxes(self):
        self.assertEqual(
            SimpleSolver._solve_line([None] * 10, [8]),
            [None, None, True, True, True, True, True, True, None, None]
        )
        self.assertEqual(
            SimpleSolver._solve_line([None] * 10, [4, 3]),
            [None, None, True, True, None, None, None, True, None, None]
        )

    def test_simple_spaces(self):
        self.assertEqual(
            SimpleSolver._solve_line([None, None, None, True, None, None, None, None, True, None], [3, 1]),
            [False, None, None, True, None, None, False, False, True, False]
        )

    def test_forcing(self):
        self.assertEqual(
            SimpleSolver._solve_line([None, None, None, None, False, None, False, None, None, None], [3, 2]),
            [None, True, True, None, False, False, False, None, True, None]
        )

    def test_glue(self):
        self.assertEqual(
            SimpleSolver._solve_line([None, None, True, None, None, None, None, None, None, None], [5]),
            [None, None, True, True, True, None, None, False, False, False]
        )
        self.assertEqual(
            SimpleSolver._solve_line([True, None, False, None, True, None, None, None, None, None], [1, 3]),
            [True, False, False, None, True, True, None, False, False, False]
        )

    def test_joining_and_splitting(self):
        self.assertEqual(
            SimpleSolver._solve_line([None, None, True, True, None, True, True, None, None, None, True, None, True, None, None], [5, 2, 2]),
            [False, False, True, True, True, True, True, False, False, True, True, False, True, True, False]
        )