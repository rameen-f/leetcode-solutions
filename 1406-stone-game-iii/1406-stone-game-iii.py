class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s1, s2, s3 = 0, 0, 0
        total = 0

        for value in reversed(stoneValue):
            total += value
            s1, s2, s3 = total - min(s1, s2, s3), s1, s2
            
        bob = total - s1
        if s1 > bob:
            return "Alice"
        if s1 < bob:
            return "Bob"
        if s1 == bob:
            return "Tie"