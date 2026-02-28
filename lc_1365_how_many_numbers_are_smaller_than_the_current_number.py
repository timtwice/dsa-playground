"""
LeetCode 1365 – Find Missing Elements
Difficulty: Easy
Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Topic: Mid Level, Array, Hash Table, Sorting, Counting Sort
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        lookup = {}

        for i, num in enumerate(sorted_nums):
            if num not in lookup:
                lookup[num] = i
        
        return [lookup[x] for x in nums]