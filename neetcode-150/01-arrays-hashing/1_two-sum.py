"""1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map: dict[int, int] = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[n] = i
        return []
