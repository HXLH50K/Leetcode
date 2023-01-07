class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        j = 1
        tar = sum(nums) - x
        tmp = nums[0]
        res = []
        while j <= len(nums):
            if i > j:
                break
            if tmp == tar:
                res.append(len(nums) - (j - i))
                if i < len(nums):
                    tmp -= nums[i]
                i += 1
                continue
            if tmp < tar:
                if j != len(nums):
                    tmp += nums[j]
                j += 1
            if tmp > tar:
                if i < len(nums):
                    tmp -= nums[i]
                i += 1
        return min(res) if res else -1
