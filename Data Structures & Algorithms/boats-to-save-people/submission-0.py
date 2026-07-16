class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        n = len(people)
        boats_used = 0

        people.sort()

        l,r = 0,n-1 
        while l<=r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            boats_used += 1
        return boats_used

