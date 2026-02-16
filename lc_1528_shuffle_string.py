"""
LeetCode 1528 – Shuffle String
Difficulty: Easy
Link: https://leetcode.com/problems/shuffle-string/
Topic: Mid Level, Array, String
"""

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        shuffled = [''] * len(s)

        for i, pos in enumerate(indices):
            shuffled[pos] = s[i]
        return ''.join(shuffled)
