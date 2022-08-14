# %%
class Solution:

    def reformat(self, s: str) -> str:
        s = sorted(s)
        n = len(s)
        num_first = True
        if n % 2 != 0:
            if 'a' <= s[n //
                        2] <= 'z' and 'a' <= s[n // 2 - 1] <= 'z' or '0' <= s[
                            n // 2] <= '9' and '0' <= s[n // 2 + 1] <= 9:
                return ""
            if '0' <= s[n // 2] <= '9':
                num_first = True
            else:
                num_first = False
        else:
            if 'a' <= s[n // 2 - 1] <= 'z' or '0' <= s[n // 2] <= '9':
                return ""

        res = ""
        i = 0
        j = n // 2 - 1
        while not 'a' <= s[j] <= 'z':
            j += 1
        while j < n:
            if num_first:
                res += s[i]
                i += 1
                res += s[j]
                j += 1
            else:
                res += s[j]
                j += 1
                res += s[i]
                i += 1

        return res


a = Solution()
a.reformat("123abc")
# %%
