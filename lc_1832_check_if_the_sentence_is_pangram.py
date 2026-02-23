"""
LeetCode 1832 – Check if the Sentence Is Pangram
Difficulty: Easy
Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Topic: Mid Level, Hash Table, String
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        found = set()

        for char in sentence:
            if char not in found:
                found.add(char)
        
        return len(found) == 26
        

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        return len(set(sentence)) == 26
        