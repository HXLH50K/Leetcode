from collections import defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        mapp = defaultdict(list)
        for i, c in enumerate(s):
            if c != "*":
                mapp[c].append(i)
                continue
            for k in sorted(mapp):
                if mapp[k]:
                    mapp[k].pop()
                    break
        res = [""] * len(s)
        for k in mapp:
            for i in mapp[k]:
                print(k, i)
                res[i] = k
        return "".join(res)
