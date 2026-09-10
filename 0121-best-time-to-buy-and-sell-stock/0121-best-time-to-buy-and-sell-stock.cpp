class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int low = prices[0];
        int profit = 0;
        
        for(int i:prices){
            if(i<low){
                low = i;
            }
            profit = i-low;
            max_profit = max(max_profit,profit);
        }
        return max_profit;
    }
};