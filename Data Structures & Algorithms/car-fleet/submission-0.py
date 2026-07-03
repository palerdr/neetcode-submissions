class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: return 0
        n = len(position)
        if n == 1: return 1

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos,spd in cars:
            ttt = (target - pos)/spd
            if not stack or ttt > stack[-1]:
                stack.append(ttt)

        return len(stack)
