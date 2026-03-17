"""
LeetCode 1929 – Concatenation of Array
Difficulty: Easy
Link: https://leetcode.com/problems/concatenation-of-array/
Topic: Mid Level, Array, Simulation
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        n2 = 2 * n
        ans = [0] * n2

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + n] = num
        
        return ans
        

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums