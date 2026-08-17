from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # The window size must be equal to the length of s1
        k = len(s1)

        # Count the frequency of characters in s1
        s1_count = Counter(s1)

        # Count the frequency of the first window in s2
        window_count = Counter(s2[:k])

        # Check the first window
        if window_count == s1_count:
            return True

        # Slide the window through the rest of s2
        for i in range(k, len(s2)):

            # Add the new character entering the window
            window_count[s2[i]] += 1

            # Remove the character leaving the window
            window_count[s2[i - k]] -= 1

            # Remove characters whose frequency becomes zero
            if window_count[s2[i - k]] == 0:
                del window_count[s2[i - k]]

            # Check if the current window is a permutation of s1
            if window_count == s1_count:
                return True

        # No permutation was found
        return False
        