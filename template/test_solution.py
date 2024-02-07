"""Test correctness of the Solution class and speed of functions."""
import unittest
import timeit
from typing import Callable

from solution import Solution

# Set of predetermined data to imput into a function,
# and data to check if said function outputs properly.
test_case = {
}
solution = Solution()
# My solutions.
my_funcs = [solution.solve1]
# Other's solutions to compare execution time.
other_funcs = [solution.other1]

# Preparations.


def call_func(func: list[Callable], **kwargs):
    """Remove need to pass parameters in test functions."""
    pass

def return_solution():
    """Return the test case solution."""
    pass

def extract_result(result):
    """Extract comparable information from the result."""
    pass

class TestSolution(unittest.TestCase):
    """Class to test the functions of the Solution class."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_solutions(self):
        for func in my_funcs:
            result = call_func(func)
            result = extract_result(result)
            self.assertEqual(result, return_solution())

    @unittest.skipIf(len(other_funcs), 0)
    def test_other_solutions(self):
        for func in other_funcs:
            result = call_func(func)
            result = extract_result(result)
            self.assertEqual(result, return_solution())

def speed_test(funcs: list[Callable], msg: str) -> None:
    print('\n', msg)
    for i, func in enumerate(funcs):
        time_took = timeit.timeit(lambda: call_func(func))
        print(f"Execution {i + 1}: {time_took}s")

def main():
    test = unittest.main(exit=False)
    if test.result.wasSuccessful():
        print("\nTests Successful. Results:")
        speed_test(my_funcs, "Testing my functions...")
        speed_test(other_funcs, "Testing other's functions...")

if __name__ == '__main__':
    main()
