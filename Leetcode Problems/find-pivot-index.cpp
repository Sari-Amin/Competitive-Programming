class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int len = nums.size();
        int total = 0, lsum = 0;
        for (int i = 0; i < len; i++)
        {
            total += nums[i];
        }
        for (int i = 0; i < len; i++)
        {
            lsum += nums[i];
            if (lsum == total - lsum + nums[i]) return i;
        }
        return -1;
    }
};