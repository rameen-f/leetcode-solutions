class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Store elements from the current window
        window = set()

        for i in range(len(nums)):

            # If the current value is already in the window,
            # a duplicate exists within distance k
            #if its distance will be greater than k it will already removed by removing step
            if nums[i] in window:
                return True

            # Add the current value to the window
            window.add(nums[i])

            # Keep the window size at most k
            if len(window) > k:
                window.remove(nums[i - k])

        # No nearby duplicate was found
        return False
        