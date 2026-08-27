"""238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Output array doesn't count against space complexity per problem constraints.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # prefix pass
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]

        # suffix pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
