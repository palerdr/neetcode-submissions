impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut lo = prices[0];
        for price in prices {
            if price < lo {
                lo = price;
            } else {
                max_profit = max_profit.max(price-lo)
            }
        }
        max_profit
    }
}
