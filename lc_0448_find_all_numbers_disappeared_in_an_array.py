"""
LeetCode 0448 – Find All Numbers Disappeared in an Array
Difficulty: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Topic: Array, Hash Table
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        lookup = set()
        
        for i in range(1, n + 1):
            lookup.add(i)
        
        for num in nums:
            if num in lookup:
                lookup.discard(num)
        
        return list(lookup)
        