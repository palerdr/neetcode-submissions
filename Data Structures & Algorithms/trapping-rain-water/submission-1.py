class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        trapped = 0

        lmaxes = [0]
        lmax = 0
        for i in range(l+1,r+1):
            if height[i-1] > lmax:
                lmax = height[i-1]
            lmaxes.append(lmax)
            
        rmaxes = []
        rmax = 0
        for i in range(r-1, l-1, -1):
            if height[i+1] >= rmax:
                rmax = height[i+1]
            rmaxes.append(rmax)    
        rmaxes.reverse()
        rmaxes.append(0) #last rmax should be zero

        while l<=r:
            waterat = min(lmaxes[l],rmaxes[l])-height[l]
            if waterat > 0:
                trapped += waterat
            l +=1
            
        return trapped
            