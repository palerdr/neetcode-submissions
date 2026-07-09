class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = [] #set up solution list
        sort = sorted(nums) #sort list
        for i in range(len(sort)-2): #find first number
            if i > 0 and sort[i] == sort[i - 1]: #avoids duplicate firsts in turn triplets
                continue #skips
            target = -sort[i] #sets target to negative first number
            left, right = i+1, len(sort) - 1 #initialize 2 pointers
            while left < right: #implement 2sum for new target
                summed = sort[left] + sort[right] 
                if summed == target:
                    sols.append([sort[left],sort[right],sort[i]]) #add to solution list
                    left += 1 #update loops variables
                    right -= 1
                    while left < right and sort[left] == sort[left - 1]: #avoid duplicate 2
                        left += 1
                    while left < right and sort[right] == sort[right + 1]:
                        right -= 1
                elif summed > target: 
                    right -= 1
                else:
                    left += 1 
        return sols