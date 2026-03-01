"""
LeetCode 3541 – Find Missing Elements
Difficulty: Easy
Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
Topic: Mid Level, Hash Table, String, Counting
"""

class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowels_lookup = {'a', 'e', 'i', 'o', 'u'}

        vowels = {}
        consonants = {}
        max_vowel_count = 0
        max_consonant_count = 0

        for x in s:
            if x in vowels_lookup:
                count = vowels.get(x, 0) + 1
                vowels[x] = count
                max_vowel_count = max(max_vowel_count, count)
            else:
                count = consonants.get(x, 0) + 1
                consonants[x] = count
                max_consonant_count = max(max_consonant_count, count)
        
        return max_vowel_count + max_consonant_count

        