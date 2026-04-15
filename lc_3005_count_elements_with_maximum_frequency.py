"""
LeetCode 3005 – Count Elements With Maximum Frequency
Difficulty: Easy
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
Topic: Mid Level, Array, Hash Table, Counting
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        lookup = {}
        highest = 0

        for num in nums:
            occurence = lookup.get(num, 0) + 1
            lookup[num] = occurence
            highest = max(highest, occurence)

        total = 0
        for val in lookup.values():
            if val == highest:
                total += val
        
        return total
        
        