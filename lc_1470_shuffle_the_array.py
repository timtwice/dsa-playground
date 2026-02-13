"""
LeetCode 1470 – Shuffle the Array
Difficulty: Easy
Link: https://leetcode.com/problems/shuffle-the-array/
Topic: Mid Level, Array
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        shuffled = []

        x = 0
        y = n

        while x < y and y < len(nums):
            shuffled.append(nums[x])
            shuffled.append(nums[y])

            x += 1
            y += 1
        
        return shuffled
        

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        shuffled = []

        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])

        return shuffled
        