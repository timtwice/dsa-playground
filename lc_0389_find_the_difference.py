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

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return ch
            freq[ch] -= 1

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t) - Counter(s))[0]