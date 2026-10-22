class SegmentTree:
    def __init__(self, arr, l, r):
        self.total = sum(arr[l:r+1])
        self.l = l
        self.m = None
        self.r = r
        self.left_child = None
        self.right_child = None
        m = l + (r-l)//2
        self.m = m
        if r-l < 1:
            return
        self.left_child = SegmentTree(arr, l, m)
        self.right_child = SegmentTree(arr, m+1, r)
    
    def sum_range(self, l, r):
        if self.l == l and self.r == r:
            return self.total
        elif r <= self.m:
            return self.left_child.sum_range(l,r)
        elif l > self.m:
            return self.right_child.sum_range(l,r)
        else:
            left_sum = self.left_child.sum_range(l,self.m)
            right_sum = self.right_child.sum_range(self.m+1,r)
            return left_sum + right_sum


class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums, 0, len(nums)-1)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.st.sum_range(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)