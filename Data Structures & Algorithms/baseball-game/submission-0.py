class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1 + n2)
            elif op == "D":
                n1 = stack.pop()
                stack.append(n1)
                stack.append(n1 * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)
            