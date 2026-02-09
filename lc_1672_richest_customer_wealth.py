"""
LeetCode 1672 – Richest Customer Wealth
Difficulty: Easy
Link: https://leetcode.com/problems/richest-customer-wealth/
Topic: Mid Level, Array, Matrix
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        wealths = []

        for account in accounts:
            wealth = 0
            for amount in account:
                wealth += amount
            wealths.append(wealth)

        richest = 0
        for w in wealths:
            richest = max(richest, w)

        return richest
        