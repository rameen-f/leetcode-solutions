
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        size: int = len(nums)

        nums.sort()
        ans: list[int] = []
        for i in range(0, size):
            if nums[i] == target:
                ans.append(i)

        return ans