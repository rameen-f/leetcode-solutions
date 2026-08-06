class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(num):
            prod = 1
            while num:
                prod *= num % 10
                num //= 10
            return prod

        while True:
            if digitProduct(n) % t == 0:
                return n
            n += 1
        