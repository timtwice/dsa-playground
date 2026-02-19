"""
LeetCode 1684 – Count the Number of Consistent Strings
Difficulty: Easy
Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/
Topic: Mid Level, Array, Hash Table, String, Bit Manipulation, Counting
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed_set = set(allowed)
        count = 0

        for word in words:
            if all(char in allowed_set for char in word):
                count += 1
        
        return count
        