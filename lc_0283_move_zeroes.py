"""
LeetCode 0283 – Move Zeroes
Difficulty: Easy
https://leetcode.com/problems/move-zeroes/
Topic: Array, Two Pointers
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = 0
        
        for i in range(n):
            num = nums[i]
            if num != 0:
                nums[k] = num
                k += 1
        
        for i in range(k, n):
            nums[i] = 0     
           