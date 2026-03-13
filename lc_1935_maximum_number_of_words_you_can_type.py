"""
LeetCode 1935 – Maximum Number of Words You Can Type
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
Topic: Mid Level, Hash Table, String
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        typed = 0
        broken = set(brokenLetters)

        for word in text.split():
            if all(ch not in broken for ch in word):
                typed += 1

        return typed


        