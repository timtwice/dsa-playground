"""
LeetCode 0628 – Maximum Product of Three Numbers
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
Topic: Array, Math, Sorting
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        first_max = second_max = third_max = float('-inf')
        first_min = second_min = float('+inf')

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num
            
            if num < first_min:
                second_min = first_min
                first_min = num
            elif num < second_min:
                second_min = num
        
        x = first_max * second_max * third_max
        y = first_max * first_min * second_min

        return max(x, y)
        