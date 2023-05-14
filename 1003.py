# %%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            stack.append(x)
            if len(stack) < 3:
                continue
            if stack[-3:] == ["a", "b", "c"]:
                stack = stack[:-3]
        return len(stack) == 0
