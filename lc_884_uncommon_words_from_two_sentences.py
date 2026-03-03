"""
LeetCode 884 – Uncommon Words from Two Sentences
Difficulty: Easy
Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
Topic: Mid Level, Hash Table, String, Counting
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        lookup = {}

        split_s1 = s1.split()
        split_s2 = s2.split()

        combined = split_s1 + split_s2
        
        for word in combined:
            lookup[word] = lookup.get(word, 0) + 1
        
        return [word for word, count in lookup.items() if count == 1]

        