class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #counting sort
        n = len(people)
        m = max(people)
        counts = [0] * (m + 1)
        for weight in people:
            counts[weight] += 1
        
        #prefix sum
        for i in range(1, m+1):
            counts[i] += counts[i-1]
        
        sorted_weights = [0] * n
        for j in range(n-1, -1, -1):
            weight = people[j]
            sorted_weights[counts[weight] - 1] = weight
            counts[weight] -= 1
        
        boats_used = 0
        l,r = 0,n-1
        while l<=r:
            total = sorted_weights[l] + sorted_weights[r]
            if total > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            boats_used += 1
        return boats_used


