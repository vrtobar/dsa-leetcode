"""217. Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return len(nums) != len(set(nums))
