from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        # Deque stores indices, not values
        dq = deque()

        # Result array
        result = []

        # Process every element
        for i in range(n):

            # 1. Remove indices that are outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Start adding results when the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        