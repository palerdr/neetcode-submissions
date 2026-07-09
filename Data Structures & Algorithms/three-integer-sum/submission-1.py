class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        n = sorted(nums)

        for i,num in enumerate(n):
            target = -num
            l = 0
            r = len(n)-1
            while l<r and i != l and i != r:
                eq = n[l] + n[r]
                if eq > target:
                    r -= 1
                elif eq < target:
                    l += 1
                else:
                    sol = sorted([n[l],n[r],n[i]])
                    if sol not in solutions:
                        solutions.append(sol)
                    l += 1

        return solutions
