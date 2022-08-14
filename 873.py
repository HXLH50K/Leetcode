#%%
from typing import List
import bisect


class Solution:

    def subArr(self, index, subarr):
        print(subarr, self.res)
        if index == len(self.arr):
            if len(subarr) > 3 and subarr[-1] == subarr[-2] + subarr[-3]:
                self.res = max(self.res, len(subarr))
            return
        if len(subarr) < 3 or subarr[-1] == subarr[-2] + subarr[-3]:
            self.subArr(index + 1, subarr)
            self.subArr(index + 1, subarr + [self.arr[index]])
        else:
            self.res = max(self.res, len(subarr) - 1)
            return

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        self.arr = arr
        self.res = 0
        self.subArr(0, [])
        return self.res if self.res > 2 else 0


# class Solution:

#     def lenLongestFibSubseq(self, arr: List[int]) -> int:
#         res = 0
#         for i in range(len(arr) - 2):
#             for j in range(i + 1, len(arr) - 1):
#                 subarr = [arr[i], arr[j]]
#                 while True:
#                     k = bisect.bisect_left(arr, subarr[-2] + subarr[-1])
#                     if k < len(arr) and arr[k] == subarr[-2] + subarr[-1]:
#                         subarr.append(subarr[-2] + subarr[-1])
#                     else:
#                         break
#                 res = max(res, len(subarr))
#         return res if res > 2 else 0

a = Solution()
a.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
# a.lenLongestFibSubseq([1,3,7,11,12,14,18])

# %%
