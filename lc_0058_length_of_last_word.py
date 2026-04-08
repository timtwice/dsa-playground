"""
LeetCode 0058 – Length of Last Word
Difficulty: Easy
Link: https://leetcode.com/problems/length-of-last-word/
Topic: String
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        last_word = ''

        for word in s.split(' '):
            if word.strip():
                last_word = word
        
        return len(last_word)
        

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        