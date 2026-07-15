class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = 0,0,0
        work = [0] * (n + m)
        while k < n + m:
            if i > m-1:
                work[k] = nums2[j]
                j += 1
            elif j > n-1:
                work[k] = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                work[k] = nums1[i]
                i += 1
            else:
                work[k] = nums2[j]
                j += 1
            k += 1
        
        nums1[:]=work



