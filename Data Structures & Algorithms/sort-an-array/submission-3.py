#merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums1, nums2):
            #merge 2 SORTED arrays
            n = len(nums1)
            m = len(nums2)
            work_array = [0] * (n + m)
            i = 0
            j = 0
            k = 0
            while k < n + m:
                if i < n and j < m:
                    if nums1[i] > nums2[j]:
                        work_array[k] = nums2[j]
                        j += 1
                    else:
                        work_array[k] = nums1[i]
                        i += 1
                elif i < n:
                    work_array[k] = nums1[i]
                    i += 1
                else:
                    work_array[k] = nums2[j]
                    j += 1
                k += 1
            return work_array

        def merge_sort(arr):
            l = len(arr)
            if l <= 1:
                return arr
            else:
                i = l // 2
                s1 = merge_sort(arr[:i])
                s2 = merge_sort(arr[i:])
                return merge(s1, s2)

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                if nums[i] < nums[i-1]:
                    return merge_sort(nums)
        return nums