class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #result at ith index is the number of days after the ith day before a warmer future temp
        # 0 if no warmer temperature exists
        n = len(temperatures)
        stack = []
        more = [0] * n

        for i,temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                more[j] = i-j

            stack.append(i)
        
        return more

