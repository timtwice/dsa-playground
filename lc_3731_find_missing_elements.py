"""
LeetCode 3731 – Find Missing Elements
Difficulty: Easy
Link: https://leetcode.com/problems/find-missing-elements/
Topic: Mid Level, Array, Hash Table, Sorting
"""

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        missing = []

        n = len(sorted_nums)

        smallest = sorted_nums[0]
        biggest = sorted_nums[n - 1]

        for num in range(smallest, biggest):
            if num not in nums:
                missing.append(num)
        
        return missing


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        nums_set = set(nums)
        missing = []
        low, high = min(nums), max(nums)

        for i in range(low, high):
            if i not in nums_set:
                missing.append(i)
        
        return missing