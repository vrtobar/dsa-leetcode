"""271. Encode and Decode Strings (Medium)
https://leetcode.com/problems/encode-and-decode-strings/

Time:  O(n)
Space: O(n)
"""


class Codec:
    def encode(self, strs: list[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1 : i])

        return res
