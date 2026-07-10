class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        n,m = len(A), len(B)
        total = n + m
        half = (total + 1) // 2

        l,r = 0,n
        while l<=r:
            x = (l + r) // 2
            y = half - x
            Almax = A[x-1] if x > 0 else float('-inf')
            Armin = A[x] if x < n else float('inf')
            Blmax = B[y-1] if y > 0 else float('-inf')
            Brmin = B[y] if y < m else float('inf')
            #golden case we found median
            if Almax <= Brmin and Blmax <= Armin:
                if total % 2 != 0:
                    return float(max(Almax, Blmax))
                return (max(Almax, Blmax) + min(Armin, Brmin)) / 2.0
            # A left max is larger than B right min, we need less items from A to the left of median
            elif Almax > Brmin:
                r = x - 1
            # Only case left is Blmax larger than Armin, we need more items from A to the left of median'
            else:
                l = x + 1


