"""Test correctness of the Solution class and speed of functions."""
import unittest
import timeit
from typing import Callable

from solution import Solution


# Set of predetermined data to imput into a function,
# and data to check if said function outputs properly.
test_case = {
    'input1' : [2, 5, 7, 5, 9, 1],
    'target1' : 10,
    'solution1' : [1, 3],
}
solution = Solution()
# My solutions.
my_funcs = [solution.solve1, solution.solve2]
# Other's solutions to compare execution time.
other_funcs = [solution.other1]

def call_func(func: list[Callable], **kwargs):
    """Remove need to pass parameters in test functions."""
    input1 = kwargs.get('input1', test_case['input1'])
    target1 = kwargs.get('target1', test_case['target1'])
    return func(input1, target1)

def return_solution():
    """Return the test case solution."""
    return test_case['solution1']

class TestSolution(unittest.TestCase):
    """Class to test the functions of the Solution class."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    """ Before adding call_func() and return_solution()
    def test_my_solutions(self):
        for func in my_funcs:
            result = func(test_case['input1'], test_case['target1'])
            self.assertEqual(result, test_case['solution1'])
    """

    def test_my_solutions(self):
        for func in my_funcs:
            result = call_func(func)
            self.assertEqual(result, return_solution())

    @unittest.skipIf(not len(other_funcs), 'No functions found.')
    def test_other_solutions(self):
        for func in other_funcs:
            result = call_func(func)
            self.assertEqual(result, return_solution())

def speed_test(funcs: list[Callable], msg: str) -> None:
    print('\n', msg)
    for i, func in enumerate(funcs):
        time_took = timeit.timeit(lambda: call_func(func))
        print(f"Function {i + 1}: {time_took}s")

def main():
    test = unittest.main(exit=False)
    if test.result.wasSuccessful():
        print("\nTests Successful. Results:")
        speed_test(my_funcs, "Testing my functions...")
        speed_test(other_funcs, "Testing other's functions...")

if __name__ == '__main__':
    main()
