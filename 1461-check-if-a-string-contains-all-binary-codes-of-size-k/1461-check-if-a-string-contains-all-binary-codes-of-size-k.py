class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # Store all unique binary codes of size k
        codes = set()

        # Check every substring of size k
        for i in range(len(s) - k + 1):

            # Add the current binary code to the set
            codes.add(s[i:i + k])

        # Check if all possible binary codes are present
        return len(codes) == 2 ** k
        