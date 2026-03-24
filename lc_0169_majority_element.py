"""
LeetCode 0169 – Majority Element
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/
Topic: Array, Hash Table, Divide and Conquer, Sorting, Counting
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        threshold = len(nums) // 2

        lookup = {}

        for num in nums:
            if num in lookup:
                lookup[num] = lookup.get(num, 0) + 1
            else:
                lookup[num] = 1
            
            if lookup[num] > threshold:
                return num
        