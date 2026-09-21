class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            new_dp[rem] += 1

            for r in range(k):
                new_rem = (r * rem) % k
                new_dp[new_rem] += dp[r]

            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result