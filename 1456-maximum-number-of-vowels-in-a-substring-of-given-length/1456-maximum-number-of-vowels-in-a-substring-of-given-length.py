class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set("aeiou")

        # Count vowels in the first window of size k
        vowel_count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = vowel_count

        # Slide the window through the remaining characters
        for i in range(k, len(s)):

            if s[i] in vowels:
                vowel_count += 1

            if s[i - k] in vowels:
                vowel_count -= 1

            max_count = max(max_count, vowel_count)

        return max_count
        