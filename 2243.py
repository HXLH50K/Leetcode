class Solution:
    def digitSum(self, s: str, k: int) -> str:
        subs = []
        while len(s) > k:
            subs = [s[i:i + k] for i in range(0, len(s), k)]
            subs = [str(sum(map(int, sub))) for sub in subs]
            s = "".join(subs)
        return s