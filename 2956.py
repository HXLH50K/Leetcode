class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0, 0]
        for x in nums1:
            if x in nums2:
                res[0] += 1
        for x in nums2:
            if x in nums1:
                res[1] += 1
        return res
