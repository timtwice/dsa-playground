"""
LeetCode 1748 – Sum of Unique Elements
Difficulty: Easy
Link: https://leetcode.com/problems/sum-of-unique-elements/
Topic: Array, Hash Table, Counting
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)

        unique_sum = 0
        for num, count in freq.items():
            if count == 1:
                unique_sum += num
        
        return unique_sum
        
        