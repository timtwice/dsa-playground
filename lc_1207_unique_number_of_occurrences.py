"""
LeetCode 1207 – Unique Number of Occurrences
Difficulty: Easy
Link: https://leetcode.com/problems/unique-number-of-occurrences/
Topic: Array, Hash Table
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        lookup = {}

        for num in arr:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1

        seen = set()

        for val in lookup.values():
            if val in seen:
                return False
            seen.add(val)
        
        return True
      

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        seen = set()
        counts = Counter(arr)

        for val in counts.values():
            if val in seen:
                return False
            seen.add(val)
        
        return True
        