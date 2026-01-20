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

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for i in range(n):
            num = abs(nums[i])
            index = num - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
                
        disappeared = []
        for i in range(n):
            if nums[i] > 0:
                disappeared.append(i + 1)
                
        return disappeared