class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 #initializes loop from left and right
        while left < right: #begins loop with 2 outermost
            sum = numbers [left] + numbers [right] #adds the two
            if sum == target:
                return [left + 1, right + 1] #singly indexed
            elif sum > target: #since right is larger if overshoot come backward one 
                right -= 1
            else:
                left += 1 #left smaller so undershoot come forward one