class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # 前缀异或和哈希表记录每个前缀异或和出现的次数
        xor_count = {0: 1}  # 初始空前缀的异或和为0，出现1次
        curr_xor = 0  # 当前前缀异或和
        result = 0

        for num in nums:
            # 计算当前位置的前缀异或和
            curr_xor ^= num

            # 如果curr_xor之前出现过，说明中间这段子数组的异或和为0
            # 因为 a ^ b = 0 => a = b
            # 所以如果某个前缀异或和等于当前的前缀异或和，则它们之间的子数组异或和为0
            result += xor_count.get(curr_xor, 0)

            # 更新前缀异或和的出现次数
            xor_count[curr_xor] = xor_count.get(curr_xor, 0) + 1

        return result
