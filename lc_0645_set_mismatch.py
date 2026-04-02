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
        