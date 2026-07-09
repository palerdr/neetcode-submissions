class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        n = len(nums)

        for i in range(n-1):
            num = nums[i]
            pre.append(num * pre[-1])
        
        for i in range(n-1, 0, -1):
            num = nums[i]
            post.append(num * post[-1])

        post.reverse()

        return [pre[i] * post[i] for i in range(n)]