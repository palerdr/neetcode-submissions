class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l,r = 0, 1000
        for i, (passengers, frm , To) in enumerate(trips):
            r = max(frm,r)
            l = min(frm,l)

        N = r-l+1
        changes = [0]*(N)

        for i, (passengers, frm , to) in enumerate(trips):
            changes[frm-l] += passengers
            if To-l < N:
                changes[to-l] -= passengers
        
        deltap = 0
        for change in changes:
            deltap += change
            if deltap > capacity:
                return False
        return True


            

            
            