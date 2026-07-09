class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False # boolean flag
        i = 0 # set up counter
        answer = [] # set up answer list
        while found == False and i < len(nums): #set up loop
            for j in range(len(nums)): # add all the other terms
                if nums[i] + nums[j] == target and i != j: #update loop condition
                    found = True
                    answer.append(i) # add to answer list to keep these variables same
                    answer.append(j)
            i += 1 #progress thru loop
        return sorted(answer) #return sorted indices

