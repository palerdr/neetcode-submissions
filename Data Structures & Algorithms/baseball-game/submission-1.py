class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        stack = []
        for op in operations:
            if op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1 + n2)
                x += n1 + n2
            elif op == "D":
                n1 = stack.pop()
                stack.append(n1)
                stack.append(n1 * 2)
                x += n1 * 2
            elif op == "C":
                n1 = stack.pop()
                x -= n1
            else:
                stack.append(int(op))
                x += int(op)
        
        return x
            