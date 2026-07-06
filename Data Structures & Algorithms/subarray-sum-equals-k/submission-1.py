class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        psum = 0
        store = {0:1}
        #prefix[r] - prefix[k] = k ---> prefix[l] = prefix[r] - k
        for num in nums:
            psum += num
            if psum - k in store:
                count += store[psum-k]
            store[psum] = store.get(psum, 0) + 1
        return count
