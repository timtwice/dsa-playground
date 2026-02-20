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

        