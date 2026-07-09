class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while numbers[l] + numbers[r] != target: #safe loop guard, guarenteed one sol
            eq = numbers[l] + numbers[r] 
            if eq > target:
                r -= 1
            else:
                l += 1
        return [l+1,r+1] #since it's 1 indexed