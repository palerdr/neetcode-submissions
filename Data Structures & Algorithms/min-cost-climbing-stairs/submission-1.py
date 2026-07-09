class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            #start with 3 back and compute cost to get to end down to 0th index
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])