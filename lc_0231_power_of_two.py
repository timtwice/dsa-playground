"""
LeetCode 0231 – Power Of Two
Difficulty: Easy
Link: https://leetcode.com/problems/power-of-two/
Topic: Math, Bit Manipulation, Recursion
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False

            n //= 2
        
        return True

        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)