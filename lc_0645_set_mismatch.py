"""
LeetCode 0645 – Set Mismatch
Difficulty: Easy
Link: https://leetcode.com/problems/set-mismatch/
Topic: Array, Hash Table, Bit Manipulation, Sorting
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        dup = 0
        missing = 0

        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                dup = i
            elif count[i] == 0:
                missing = i

        return [dup, missing]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        missing = 0

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                dup = abs(num)
            else:
                nums[idx] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        
        return [dup, missing]

        