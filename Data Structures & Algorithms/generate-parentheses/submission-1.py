class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        stack = []

        def dfs(left, right):
            if left == right == n:
                ret.append("".join(stack))
                return
            
            if left < n:
                stack.append("(") #don't add, append then join strings immutable
                dfs(left+1, right)
                stack.pop()

            if right < left:
                stack.append(")") 
                dfs(left, right+1)
                stack.pop() #backtrack after both

        dfs(0,0)
        return ret
