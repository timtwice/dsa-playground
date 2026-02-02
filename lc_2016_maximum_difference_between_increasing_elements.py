"""
LeetCode 2016 – Maximum Difference Between Increasing Elements
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
Topic: Array
"""

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        min_num = nums[0]
        diff = -1

        for num in nums[1:]:
            if num > min_num:
                diff = max(diff, num - min_num)
            else:
                min_num = num
        
        return diff

        