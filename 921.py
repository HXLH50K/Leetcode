# %%
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        s = list(s)
        while s:
            c = s.pop(0)
            if not stack:
                stack.append(c)
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)

a = Solution()
a.minAddToMakeValid(")())(")