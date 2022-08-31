# %%
class Solution:

    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        stack = []
        while pushed:
            if not stack:
                stack.append(pushed.pop(0))
                continue
            if stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                continue
            stack.append(pushed.pop(0))
        while popped or stack:
            if popped.pop(0) != stack.pop(-1):
                return False
        return not popped and not stack