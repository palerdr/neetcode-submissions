from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        @lru_cache(None)
        def waysToTake(i, amount):
            if i == len(coins):
                return 1 if amount == 0 else 0

            take = 0
            if coins[i] <= amount:
                take = waysToTake(i, amount-coins[i])
            skip = waysToTake(i+1, amount)

            return take + skip

        
        return waysToTake(0, amount)
            

        