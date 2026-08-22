"""242. Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map: dict[str, int] = {}

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char_map.get(char, 0) == 0:
                return False
            char_map[char] -= 1

        return True


# from collections import Counter


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)
