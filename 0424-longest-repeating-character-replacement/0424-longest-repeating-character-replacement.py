class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l = 0

        # Store the frequency of each uppercase character
        count = [0] * 26

        # Expand the window using the right pointer
        for r in range(len(s)):

            # Increase frequency of the current character
            count[ord(s[r]) - 65] += 1

            # Shrink the window if more than k replacements are needed
            while (r - l + 1) - max(count) > k:

                # Remove the leftmost character from the window
                count[ord(s[l]) - 65] -= 1

                # Move the left pointer forward
                l += 1

            # Update the longest valid window
            longest = max(r - l + 1, longest)

        return longest
        