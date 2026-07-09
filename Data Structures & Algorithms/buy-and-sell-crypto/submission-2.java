class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        int i=0;
        while (i < prices.length-1){//can't buy on the last day
        for (int j = i+1; j < prices.length; j++){
            int profit = prices[j] - prices[i];
            if (profit >= maxprofit){
                maxprofit = profit;
            }
        }
        i++;
    }
    return maxprofit;
}
}