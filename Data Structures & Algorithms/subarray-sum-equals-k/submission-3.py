class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        store = {}
        prefix = 0
        for i in range(n+1):
            if prefix in store:
                ans += store[prefix]
            
            if prefix + k not in store:
                store[prefix + k] = 0
            store[prefix + k] += 1
            
            if i < n:
                prefix += nums[i]
                
        return ans


        