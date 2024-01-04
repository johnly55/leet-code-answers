"""Test correctness of the Solution class and speed of functions."""
import unittest
import timeit
from typing import Callable

from solution import Solution


# Set of predetermined data to imput into a function,
# and data to check if said function outputs properly.
test_case = {
    'problem1' : [2, 5, 7, 5, 9, 1],
    'target1' : 10,
    'solution1' : [1, 3],
}
solution = Solution()
# My solutions.
my_funcs = [solution.solve1, solution.solve2]
# Other's solutions to compare execution time.
other_funcs = [solution.other1]

class TestSolution(unittest.TestCase):
    """Class to test the functions of the Solution class."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_solutions(self):
        for func in my_funcs:
            result = func(test_case['problem1'], test_case['target1'])
            self.assertEqual(result, test_case['solution1'])

    @unittest.skipIf(len(other_funcs), 0)
    def test_other_solutions(self):
        for func in other_funcs:
            result = func(test_case['problem1'], test_case['target1'])
            self.assertEqual(result, test_case['solution1'])

def speed_test(funcs: list[Callable], msg: str) -> None:
    print('\n', msg)
    for i, func in enumerate(funcs):
        time_took = timeit.timeit(lambda: func(test_case['problem1'], test_case['target1']))
        print(f"Execution {i + 1}: {time_took}s")

def main():
    test = unittest.main(exit=False)
    if test.result.wasSuccessful():
        print("\nTests Successful. Results:")
        speed_test(my_funcs, "Testing my functions...")
        speed_test(other_funcs, "Testing other's functions...")

if __name__ == '__main__':
    main()
