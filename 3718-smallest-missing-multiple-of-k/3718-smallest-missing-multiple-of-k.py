class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = [False] * 101

        for num in nums:
            present[num] = True

        multiple = k
        while True:
            if multiple > 100 or not present[multiple]:
                return multiple
            multiple += k
        return multiple