"""
LeetCode 0027 – Remove Element
Difficulty: Easy
Link: https://leetcode.com/problems/remove-element/
Topic: Array, Two Pointers
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        right = 0
        left = len(nums)
        
        while right < left:
            if nums[right] == val:
                nums[right] = nums[left - 1]
                left -= 1
            else:
                right += 1
            
        return right


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        
        return count