class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        q = deque([amount])
        v = set()
        coins_used = 0
        while q:
            for _ in range(len(q)):
                current_amount = q.popleft()
                if current_amount == 0:
                    return coins_used

                elif current_amount < 0 or current_amount in v:
                    continue
                    
                v.add(current_amount)
                for coin in coins:
                    q.append(current_amount - coin)
            coins_used += 1
        
        return -1 