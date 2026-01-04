"""
LeetCode 1295 – Find Numbers With Even Number Of Digits
Difficulty: Easy
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Topic: Array, Math
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0

        for num in nums:
            if self.is_even_digit(num):
                even_digit_count += 1

        return even_digit_count

    def is_even_digit(self, num: int) -> bool:
        count = 0
        while num > 0:
            num //= 10
            count += 1 
        return count % 2 == 0
        

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                even_digit_count += 1

        return even_digit_count