# %%
from typing import List


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        i = j = 0
        n = len(fruits)
        if n <= 2:
            return n
        num = [[-1, -1], [-1, -1]]  #loc value
        bucket = []
        res = 0
        while j < n:
            now = fruits[j]
            if now in list(zip(*num))[1]:
                bucket.append(fruits[j])
                if num[0][1] == now:
                    num[0][0] = j
                else:
                    num[1][0] = j
                num.sort(key=lambda x: x[0])
                j += 1
            elif num[0][0] == -1:
                num[0] = [j, now]
                bucket.append(fruits[j])
                j += 1
            elif num[1][0] == -1:
                num[1] = [j, now]
                bucket.append(fruits[j])
                j += 1
            else:
                res = max(res, len(bucket))
                i = num[0][0] + 1
                bucket = fruits[i:j]
                num.pop(0)
                num.append([j, now])
        res = max(res, len(bucket))
        return res


a = Solution()
fruits = [0, 1, 2, 2]
a.totalFruit(fruits)
# %%
