class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            reverse_value = 26 - (ord(c) - ord('a'))
            position = i + 1

            total += reverse_value * position
        return total