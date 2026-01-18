"""
LeetCode 1051 – Height Checker
Difficulty: Easy
Link: https://leetcode.com/problems/height-checker/
Topic: Array, Sorting, Counting Sort
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        k = 0
        
        for i, height in enumerate(heights):
            if height != expected[i]:
                k += 1
        
        return k