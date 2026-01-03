"""
LeetCode 0961 – N-Repeated Element in Size 2N Array
Difficulty: Easy
Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
Topic: Array, Hash Table
"""

from typing import List

"""
Initial solution.
"""
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        lookup = {} // {number: occurrence}

        for _, num in enumerate(nums):
            if num in lookup:
                occurrence = lookup[num]
                new_occurrence = occurrence + 1
                
                if new_occurrence == n: return num

                lookup[num] = new_occurrence
            else: 
                lookup[num] = 1

"""
We can further optimise the above since there is a constraint that the array contains n+1 unique elements, so there won't be any duplicates except the element that is repeated n times.
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        lookup = set()
        
        for num in nums:
            if num in lookup:
                return num

            lookup.add(num)