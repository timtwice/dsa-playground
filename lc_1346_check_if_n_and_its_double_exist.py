"""
LeetCode 1346 – Check If N and Its Double Exist
Difficulty: Easy
Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
Topic: Array, Hash Table, Two Pointers, Binary Search, Sorting
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for x in arr:
            if 2 * x in seen:
                return True
            
            if x % 2 == 0 and x // 2 in seen:
                return True

            seen.add(x)

        return False