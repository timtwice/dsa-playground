"""
LeetCode 1816 – Truncate Sentence
Difficulty: Easy
Link: https://leetcode.com/problems/truncate-sentence/
Topic: Mid Level, Array, String
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        result = ""
        splitted = s.split()

        for i in range(k):
            result 
            result = result + " " + splitted[i]

        return result.strip()
        