"""
LeetCode 349 – Intersection of Two Arrays
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-arrays/
Topic: Array, Hash Table, Two Pointers, Binary Search, Sorting
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = set(nums1)
        set2 = set(nums2)

        intersection = []

        for num in set1:
            if num in set2:
                intersection.append(num)

        return intersection

       
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))