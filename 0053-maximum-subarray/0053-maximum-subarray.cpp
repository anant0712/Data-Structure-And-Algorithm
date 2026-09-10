class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int current_sum = 0;
        int max_sum = nums[0];

        for(int n:nums){
            current_sum = max(n,current_sum+n);
            max_sum = max(max_sum,current_sum);
        }
        return max_sum;
    
    }

};