"""347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Time:  O(n)
Space: O(n)
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        freqs: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            freqs[count].append(num)

        res = []
        for bucket in reversed(freqs):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

        return res
