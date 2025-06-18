class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n, 3):
            re = nums[i : i + 3]
            if re[2] - re[0] > k:
                return []
            res.append(re)
        return res
