class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1

        for i in range(1,len(nums)):
            num = nums[i]
            if num > dp[-1]:
                dp.append(num)
                LIS += 1
            else:
                l,r = 0,len(dp)-1
                while l <= r:
                    m = (l+r)//2
                    if dp[m] >= num:
                        r = m-1
                    else:
                        l = m+1
                dp[l] = num
        
        return LIS
                    
