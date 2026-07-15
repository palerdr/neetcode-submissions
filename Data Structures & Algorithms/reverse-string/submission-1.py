class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new=''.join(s)
        s_new=new[::-1]
        s[:]=list(s_new)
