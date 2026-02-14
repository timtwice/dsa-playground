"""
LeetCode 1431 – Kids With the Greatest Number of Candies
Difficulty: Easy
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Topic: Mid Level, Array
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        result = []

        for candy in candies:
            result.append(True if candy + extraCandies >= highest else False)

        return result

        