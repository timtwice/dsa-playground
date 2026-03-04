"""
LeetCode 1394 – Find Lucky Integer in an Array
Difficulty: Easy
Link: https://leetcode.com/problems/find-lucky-integer-in-an-array/
Topic: Mid Level, Array, Hash Table, Counting
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        lucky = -1
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            if count == num:
                lucky = max(lucky, num)

        return lucky
        