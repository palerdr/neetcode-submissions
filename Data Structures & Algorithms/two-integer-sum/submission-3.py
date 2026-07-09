class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = defaultdict(int)
        s = 0
        l = 0
        for i,num in enumerate(nums): #loop through list
            diff = target - num
            if diff in numbers: #check if we have other variable
                s = min(numbers.get(diff),i)
                l = max(numbers.get(diff),i)
            else:
                numbers[num] = i #add if not
        return [s,l]
        

