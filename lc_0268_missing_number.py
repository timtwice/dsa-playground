"""
LeetCode 0268 – Missing Number
Difficulty: Easy
Link: https://leetcode.com/problems/missing-number/
Topic: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
"""

# Brute Force approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        missing = None

        for i in range(n + 1):
            if i not in nums:
                missing = i
                return missing

# Optimised approach - space O(1) and memory O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        missing_sum = 0
        actual_sum = 0

        for i in range(n + 1):
            if i < n:
                missing_sum += nums[i]
            actual_sum += i

        return actual_sum - missing_sum

             