"""
LeetCode 0258 – Add Digits
Difficulty: Easy
Link: https://leetcode.com/problems/add-digits/
Topic: Math, Simulation, Number Theory
"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num

        
class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        
        return 1 + (num - 1) % 9

        