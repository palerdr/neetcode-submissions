class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1: return True
        k = 0
        while nums[k] != 0:
            jump = nums[k]
            if k + jump >= n - 1: return True
            best_reach = 0
            best_reach_idx = k
            for i in range(k + 1, k + 1 + jump):
                reach = i + nums[i]
                if reach > best_reach:
                    best_reach = reach
                    best_reach_idx = i
            k = best_reach_idx

        return False


