# %%
from typing import List
from collections import defaultdict


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = defaultdict(lambda: "?")
        for x in knowledge:
            dic.update({"(" + x[0] + ")": x[1]})
        n = len(s)
        stack = []
        res = []
        now = res
        for x in s:
            if x == "(":
                now = stack
                now.append(x)
            elif x == ")":
                now.append(x)
                key = "".join(stack)
                res.append(dic[key])
                now = res
                stack = []
            else:
                now.append(x)
        return "".join(res)


s = "hi(name)"
knowledge = [["a", "b"]]
Solution().evaluate(s, knowledge)

# %%
