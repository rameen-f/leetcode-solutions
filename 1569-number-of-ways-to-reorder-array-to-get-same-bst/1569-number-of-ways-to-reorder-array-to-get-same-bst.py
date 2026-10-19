class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def count(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            ways = comb(len(left) + len(right), len(left))

            return (ways * count(left) * count(right)) % MOD

        return (count(nums) - 1) % MOD