"""
LeetCode 771 – Jewels and Stones
Difficulty: Easy
Link: https://leetcode.com/problems/jewels-and-stones/
Topic: Hash Table, String
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        converted_jewels = set(jewels)
        count = 0

        for stone in stones:
            if stone in converted_jewels:
                count += 1
        
        return count
        