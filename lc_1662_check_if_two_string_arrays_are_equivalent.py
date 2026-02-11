"""
LeetCode 1662 – Check If Two String Arrays are Equivalent
Difficulty: Easy
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Topic: Mid Level, Array, String
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = string2 = ""

        for w in word1:
            string1 += w
        
        for w in word2:
            string2 += w
        
        return string1 == string2

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)