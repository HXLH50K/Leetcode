class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ")":
                stack.append(c)
                continue
            new_sub_str = []
            while stack[-1] != "(":
                new_sub_str.append(stack.pop(-1))
            stack.pop(-1)
            stack.extend(new_sub_str)
        return "".join(stack)
