class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        maxi,sum=nums[0],0
        for num in nums:
            maxi=max(num,maxi)
            sum+=num
        return n*maxi-sum
        