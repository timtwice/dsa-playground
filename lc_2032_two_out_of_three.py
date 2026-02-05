"""
LeetCode 2032 – Two Out of Three
Difficulty: Easy
Link: https://leetcode.com/problems/two-out-of-three/
Topic: Mid Level, Array, Hash Table, Bit Manipulation
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list ((s1 & s2) | (s1 & s3) | (s2 & s3))
        