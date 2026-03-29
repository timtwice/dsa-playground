"""
LeetCode 0387 – First Unique Character in a String
Difficulty: Easy
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Topic: Hash Table, String, Queue, Counting
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        lookup = {}

        for ch in s:
            lookup[ch] = lookup.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if lookup[ch] == 1:
                return i

        return -1

        
class Solution:
    def firstUniqChar(self, s: str) -> int:

        counts = Counter(s)

        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1

        