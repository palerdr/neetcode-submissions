class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {
            '+',
            '-',
            '*',
            '/',
        }

        def operation(lhs, rhs, op):
            if op == '+':
                return lhs + rhs
            elif op == '-':
                return lhs - rhs
            elif op == '*':
                return lhs * rhs
            else:
                return int(lhs/rhs)


        stack = []

        for token in tokens:
            if token in operators:
                op = token
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(operation(lhs,rhs,op))
            else:
                stack.append(int(token))
        
        return stack.pop()
