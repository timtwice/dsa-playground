"""
LeetCode 2942 – Find Words Containing Character
Difficulty: Easy
Link: https://leetcode.com/problems/find-words-containing-character/
Topic: Mid Level, Array, String
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        return [i for i, word in enumerate(words) if x in word]