"""
LeetCode 1389 – Create Target Array in the Given Order
Difficulty: Easy
Link: https://leetcode.com/problems/create-target-array-in-the-given-order/
Topic: Mid Level, Array, Simulation
"""

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        target = []
        n = len(nums)

        for i, num in zip(index, nums):
            target.insert(i, num)

        return target
        