# %%
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        nums3 = []
        while nums1 != [] and nums2 != []:
            if nums1[0] <= nums2[0]:
                nums3.append(nums1.pop(0))
            else:
                nums3.append(nums2.pop(0))
        while nums1 != []:
            nums3.append(nums1.pop(0))
        while nums2 != []:
            nums3.append(nums2.pop(0))

        if len(nums3) % 2 != 0:
            res = float(nums3[(len(nums3) - 1) // 2])
        else:
            res = (nums3[len(nums3) // 2] + nums3[(len(nums3) - 1) // 2]) / 2
        return res


a = Solution()
a.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])

# %%
