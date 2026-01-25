"""
LeetCode 0136 – Single Number
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/
Topic: Array, Bit Manipulation
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        lookup = set()

        for num in nums:
            if num in lookup:
                lookup.remove(num)
            else:
                lookup.add(num)

        return lookup.pop()

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single_number = 0

        for num in nums:
            single_number ^= num

        return single_number       