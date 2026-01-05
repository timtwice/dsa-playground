"""
LeetCode 0977 – Squares of a Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Topic: Array, Two Pointers, Sorting
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        sorted_nums = [0] * n
        left, right = 0, n -1
        pos = n - 1
        
        while left <= right:
            s_left = nums[left] ** 2
            s_right = nums[right] ** 2
            
            if s_left > s_right:
                sorted_nums[pos] = s_left
                left += 1
            else:
                sorted_nums[pos] = s_right
                right -=1
            
            pos -= 1
        
        return sorted_nums

        
#         for i, num in enumerate(nums):
#             nums[i] = num * num
                
#         return sorted(nums)
            
        