# %%
class Solution:

    def maxScore(self, s: str) -> int:
        left_zero = [0]
        right_one = [0]
        for i in range(len(s)):
            if s[i] == '0':
                left_zero.append(left_zero[-1] + 1)
            else:
                left_zero.append(left_zero[-1])
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                right_one.insert(0, right_one[0] + 1)
            else:
                right_one.insert(0, right_one[0])
        res = [left_zero[i] + right_one[i] for i in range(len(left_zero))]
        return max(res[1:-1])


a = Solution()
s = "11"
a.maxScore(s)

# %%
