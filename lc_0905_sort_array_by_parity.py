"""
LeetCode 0905 – Sort Array By Parity
Difficulty: Easy
Link: https://leetcode.com/problems/sort-array-by-parity/
Topic: Array, Two Pointers, Sorting
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            if nums[l] % 2 != 0:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        
        return nums