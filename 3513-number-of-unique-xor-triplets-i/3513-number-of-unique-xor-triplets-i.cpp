class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();

        if (n < 3) {
            return n;
        }

        int p = 0, cur = n;

        while (cur) {
            cur >>= 1;
            p++;
        }

        return 1 << p;
    }
};