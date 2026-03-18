"""
LeetCode 2469 – Convert the Temperature
Difficulty: Easy
Link: https://leetcode.com/problems/convert-the-temperature/
Topic: Mid Level, Math
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
        