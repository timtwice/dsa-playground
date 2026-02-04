"""
LeetCode 2073 – Time Needed to Buy Tickets
Difficulty: Easy
Link: https://leetcode.com/problems/time-needed-to-buy-tickets/
Topic: Mid Level, Array, Queue, Simulator
"""

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        count = tickets[k]
        time = 0
        i = 0
        n = len(tickets)

        while count > 0:
            # if we have reached the end, reset to zero
            if i == n:
                i = 0
            
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1

                if i == k:
                    count -= 1
            
            i += 1

        return time

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        target = tickets[k]
        time = 0

        for i, j in enumerate(tickets):
            if i <= k:
                time += min(j, target)
            else:
                time += min(j, target - 1)

        return time