class Solution:
    def climbStairs(self, n: int) -> int:

        #ways(i) = ways(i + 1) + ways(i + 2)
        #initial recurrence
        #ways(i-2) = ways(i-1) + ways(i)
        #ways(i-3) = ways(i-2) + ways(i-1)
        ways_n_from_n = 1
        ways_n_from_n_minus_one = 1

        t1 = ways_n_from_n_minus_one
        t2 = ways_n_from_n
        #we want ways_n_from_0
        for _ in range(n-2+1):
            tmp = t1
            t1 = t1 + t2
            t2 = tmp

        return t1



        
