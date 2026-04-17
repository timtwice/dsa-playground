"""
LeetCode 3005 – Count Elements With Maximum Frequency
Difficulty: Easy
Link: https://leetcode.com/problems/count-elements-with-maximum-frequency/
Topic: Mid Level, Array, Hash Table, Counting
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        lookup = {}
        highest = 0

        for num in nums:
            occurence = lookup.get(num, 0) + 1
            lookup[num] = occurence
            highest = max(highest, occurence)

        total = 0
        for val in lookup.values():
            if val == highest:
                total += val
        
        return total
        
        
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        lookup = {}
        max_freq = 0
        total = 0

        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
            count = lookup[num]

            if count > max_freq:
                max_freq = count
                total = count
            elif count == max_freq:
                total += count
        
        return total

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        lookup = Counter(nums)
        max_freq = max(lookup.values())

        return sum(freq for freq in lookup.values() if freq == max_freq)