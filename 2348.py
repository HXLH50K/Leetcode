class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = []
        i = 0
        j = 0
        while i <= j and j < len(nums):
            if j == len(nums) - 1 and nums[j] == 0:
                zeros.append(j - i + 1)
                break
            if nums[i] != 0:
                i += 1
                j = i
                continue
            if nums[j] == 0:
                j += 1
                continue
            zeros.append(j - i)
            i = j
        res = 0
        for x in zeros:
            res += x * (x + 1) // 2
        return res
