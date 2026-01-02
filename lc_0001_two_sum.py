"""
LeetCode 0001 – Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
Topic: Array, Hash Table
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_table = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in lookup_table:
                return [lookup_table[complement], i]

            lookup_table[num] = i