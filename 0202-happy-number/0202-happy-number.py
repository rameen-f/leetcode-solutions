class Solution:
    def isHappy(self, n: int) -> bool:
        #sum of squares of digits
        def getNext(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        #check cycle exist or not
        slow = n
        fast = getNext(n)

        while slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
        