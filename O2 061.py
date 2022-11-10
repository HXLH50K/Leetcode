# %%
from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        res = []
        cnt = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                cnt += 1
                res.append([nums1[i], nums2[j]])
        res.sort(key = lambda x: sum(x))
        return res[:k]
