"""
LeetCode 0414 – Third Maximum Number
Difficulty: Easy
Link: https://leetcode.com/problems/third-maximum-number/
Topic: Array, Sorting
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        x = None
        y = None
        z = None
  
        for num in nums:
            if num == x or num == y or num == z:
                continue
            
            if x is None or num > x:
                z = y
                y = x
                x = num
            
            elif y is None or num > y:
                z = y
                y = num 
            
            elif z is None or num > z:
                z = num
                
        return z if z is not None else x