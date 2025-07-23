class Solution:
    def betterGain(self, x: int, y: int) -> int:
        if x < y:
            return "ba"
        else:
            return "ab"

    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        stack = []
        better = self.betterGain(x, y)
        not_better = "ba" if better == "ab" else "ab"
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if stack[-1] + c == better:
                res += x if better == "ab" else y
                stack.pop()
            else:
                stack.append(c)
        s = "".join(stack)
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if stack[-1] + c == not_better:
                res += y if better == "ab" else x
                stack.pop()
            else:
                stack.append(c)
        return res
