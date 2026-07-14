class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        r,w,b = 0,0,n-1
        #iterate until the partition makes w == b
        #0s 0..r-1
        #1s r..w-1
        #unprocessed w..b-1
        #2s b..n
        while w <= b:
            if nums[w] == 0:
                swap(w, r)
                r += 1
                w += 1
            elif nums[w] == 2:
                swap(w, b)
                b -= 1
            else:            
                w += 1



        