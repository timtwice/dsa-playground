"""
LeetCode 0941 – Valid Mountain Array
Difficulty: Easy
Link: https://leetcode.com/problems/valid-mountain-array/
Topic: Array
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        valid_ascent, valid_descent = False, False
        descent_index = -1
        
        if n < 3 or arr[0] >= arr[1]:
            return False
        
        valid_ascent = True
        i = 1
        
        while i < n - 1:
            if arr[i] == arr[i + 1]:
                return False
            
            if descent_index < 0:
                if arr[i] < arr[i + 1]:
                    valid_ascent = True
                else:
                    descent_index = i
                    valid_descent = True
            else:
                if arr[i] > arr[i + 1]:
                    valid_descent = True
                else:
                    return False
            
            i += 1
                    
        return valid_ascent and valid_descent


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
