class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def min_cost_path(s):
            if not s:
                return 0
            elif len(s) == 1:
                return s[0]
            return s[0] + min(min_cost_path(s[1:]), min_cost_path(s[2:]))
        return min(min_cost_path(cost), min_cost_path(cost[1:]))