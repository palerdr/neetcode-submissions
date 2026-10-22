from functools import cache
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def num_trees_rec(n):
            if n <= 1:
                return 1
            
            ans = 0
            for i in range(1,n+1):
                ans += num_trees_rec(i-1) * num_trees_rec(n-i)
            return ans
    
        return num_trees_rec(n)
