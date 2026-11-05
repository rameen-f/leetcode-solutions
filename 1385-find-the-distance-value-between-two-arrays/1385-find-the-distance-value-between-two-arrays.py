class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        w = d + 1  # two values in one bucket are at most d apart
        lo, hi = {}, {}  # smallest and largest b in each bucket
        for b in arr2:
            k = b // w
            lo[k], hi[k] = min(lo.get(k, b), b), max(hi.get(k, b), b)

        def far(a):  # own bucket empty, neighbours' closest values out of reach
            k = a // w
            return k not in lo and hi.get(k - 1, -inf) < a - d and lo.get(k + 1, inf) > a + d

        return sum(map(far, arr1))