class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = {}  # 用于记录当前选择的数字出现次数

        def backtrack(index):
            if index == len(nums):
                return 1  # 找到一个有效子集

            # 不选择当前数字
            total = backtrack(index + 1)

            # 判断是否可以选择当前数字
            curr = nums[index]
            can_pick = True
            # 检查当前数字+-k是否在已选择的数字中
            if curr + k in counter and counter[curr + k] > 0:
                can_pick = False
            if curr - k in counter and counter[curr - k] > 0:
                can_pick = False

            # 如果可以选择当前数字
            if can_pick:
                counter[curr] = counter.get(curr, 0) + 1
                total += backtrack(index + 1)
                counter[curr] -= 1
                if counter[curr] == 0:
                    del counter[curr]

            return total

        # 因为空集不算美丽子集，所以需要减1
        return backtrack(0) - 1
