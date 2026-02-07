"""
LeetCode 1372 – Find the Highest Altitude
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-highest-altitude/
Topic: Mid Level, Array, Prefix Sum
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = 0
        altitude = 0

        for i in range(len(gain)):
            altitude += gain[i]
            highest = max(highest, altitude)
        
        return highest
        