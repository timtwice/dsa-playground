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
        

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num
            
            count += 1 if num == majority else -1

        return majority
        