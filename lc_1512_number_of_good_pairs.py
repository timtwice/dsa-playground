"""
LeetCode 1512 – Number of Good Pairs
Difficulty: Easy
Link: https://leetcode.com/problems/number-of-good-pairs/
Topic: Mid Level, Array, Hash Table, Math, Counting
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        pairs = 0
        for count in freq.values():
            pairs += (count * (count - 1)) // 2

        return pairs