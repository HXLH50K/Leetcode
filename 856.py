class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
                continue
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack and stack[-1] != '(':
                        score += stack.pop()
                    stack.pop()  # pop the '('
                    stack.append(2 * score)
        return sum(stack)