"""
LeetCode 1299 – Replace Elements with Greatest Element on Right Side
Difficulty: Easy
Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Topic: Array
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        highest = -1
        
        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = highest
            highest = max(highest, current)
        
        return arr
