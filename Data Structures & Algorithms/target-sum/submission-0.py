class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = sum(nums)
        if target > t or target < -t:
            return 0

        dp = [0]*(2*t+1)
        #holds the solution to the amount at the index
        #range from -sum, 0, +sum shifted to 2t+1 indexes
        #base case, target 0 can only be made 1 way
        dp[t] = 1

        for a in nums:
            new = [0]*(2*t+1)
            for index, count in enumerate(dp):
                if count:
                #recurrence
                    if 0 <= index+a <= 2*t:
                        new[index + a] += count 
                    if 0 <= index-a <= 2*t:
                        new[index - a] += count
            
            dp = new


        #array state will be for index 0 at the end
        return dp[target + t]

