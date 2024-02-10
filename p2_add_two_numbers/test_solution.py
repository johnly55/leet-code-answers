"""Test correctness of the Solution class and speed of functions."""
import unittest
import timeit
from typing import Callable

from solution import Solution, ListNode

# Set of predetermined data to imput into a function,
# and data to check if said function outputs properly.
test_case = {
    'input1' : [2, 4, 3],
    'input2' : [5, 6, 4],
    'solution1' : [7, 0, 8],
}
solution = Solution()
# My solutions.
my_funcs = [solution.solve1, solution.solve2]
# Other's solutions to compare execution time.
other_funcs = [solution.other1]

# Preparations.
input1 = test_case['input1']
l1 = ListNode(val=input1.pop(0))
l1_ptr = l1
for input in input1:
    l1_ptr.next = ListNode(val=input)
    l1_ptr = l1_ptr.next

input2 = test_case['input2']
l2 = ListNode(val=input2.pop(0))
l2_ptr = l2
for input in input2:
    l2_ptr.next = ListNode(val=input)
    l2_ptr = l2_ptr.next

def call_func(func: list[Callable], **kwargs):
    """Remove need to pass parameters in test functions."""
    return func(l1, l2)

def return_solution():
    """Return the test case solution."""
    return test_case['solution1']

def extract_result(result):
    """Extract comparable information from the result."""
    extract_list = []
    while result is not None:
        extract_list.append(result.val)
        result = result.next
    return extract_list

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

    @unittest.skipIf(not len(other_funcs), 'No functions found.')
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
