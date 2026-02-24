"""
LeetCode 2053 – Kth Distinct String in an Array
Difficulty: Easy
Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/
Topic: Mid Level, Array, Hash Table, String, Counting
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        lookup = {}

        for s in arr:
            if s in lookup:
                lookup[s] += 1
            else:
                lookup[s] = 1
        
        distinct = []

        for key, count in lookup.items():
            if count == 1:
                distinct.append(key)

        if len(distinct) < k:
            return ""
        else:
            return distinct[k - 1]


        