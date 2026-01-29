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

        