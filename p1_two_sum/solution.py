"""Includes the Solution class to solve a problem."""


class Solution:
    """Contains functions to solve a problem."""
    # My solution
    def solve1(self, nums: list[int], target: int) -> list[int]:
        """Simple double recursion search.
        Picks one number, check rest of the list. Increment and repeat.
        Time complexity: O(n^2)

        Args:
            nums: list of numbers to pick from.
            target: desired sum of two numbers from the list.

        Returns:
            A list of the two indexes that add up to the target number 
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0,0]

    # My solution
    def solve2(self, nums: list[int], target: int) -> list[int]:
        """Uses a dictionary to save the target.
        If the current number is not in dict, add a key of (this number - target),
        and a value the current index.
        Time complexity: O(n)

        Args:
            nums: list of numbers to pick from.
            target: desired sum of two numbers from the list.

        Returns:
            A list of the two indexes that add up to the target number 
        """
        my_dict = {}
        for i, value in enumerate(nums):
            # If condition met, break early.
            if value in my_dict:
                return [my_dict[value], i]
            else:
                # Add target - value to dict as the key.
                # And add the index as the dict value.
                my_dict[target-value] = i
        return [-1,-1]

    # Other's solution
    def other1(self, nums: list[int], target: int) -> list[int]:
        """Example Docstring."""
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
