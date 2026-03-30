"""
LeetCode 0389 – Find the Difference
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-difference/
Topic: Hash Table, String, Bit Manipulation, Sorting
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        
        for ch in s:
            diff ^= ord(ch)
        for ch in t:
            diff ^= ord(ch)
        
        return chr(diff)