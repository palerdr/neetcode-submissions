class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        prof = 0

        for i in range(len(prices)):
            diff = prices[i] - prices[l]
            prof = max(prof, diff)

            #found a better entry
            if prices[i] <= prices[l]:
                l = i
            
        return prof