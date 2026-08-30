class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int minIndex = 0;
        int maxIndex = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }

            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }

        int removeFromFront = max(minIndex, maxIndex) + 1;

        int removeFromBack = n - min(minIndex, maxIndex);

        int removeFromBothSides = min(
            minIndex + 1 + (n - maxIndex),
            maxIndex + 1 + (n - minIndex)
        );

        return min(removeFromFront, min(removeFromBack, removeFromBothSides));
    }
};