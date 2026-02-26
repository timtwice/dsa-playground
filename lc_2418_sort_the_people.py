"""
LeetCode 2418 – Sort the People
Difficulty: Easy
Link: https://leetcode.com/problems/sort-the-people/
Topic: Mid Level, Array, Hash Table, String, Sorting
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        height_to_name = {}

        for name, height in zip(names, heights):
            height_to_name[height] = name

        sorted_heights = sorted(heights, reverse=True)

        return [height_to_name[height] for height in sorted_heights]


        