"""
LeetCode 3289 – The Two Sneaky Numbers of Digitville
Difficulty: Easy
Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
Topic: Mid Level, Array, Hash Table, Math
"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        lookup = set()
        sneaky = []

        for num in nums:
            if num not in lookup:
                lookup.add(num)
            else:
                sneaky.append(num)

        return sneaky
        