"""
LeetCode 0020 – Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Topic: String, Stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack or pairs[stack.pop()] != ch:
                    return False

        return not stack