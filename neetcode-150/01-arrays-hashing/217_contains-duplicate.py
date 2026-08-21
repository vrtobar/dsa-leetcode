"""217. Contains Duplicate (Easy)
https://leetcode.com/problems/<slug>/

Time:  O(?)
Space: O(?)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False
