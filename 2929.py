class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        # 遍历第一个人分到的糖果数
        for i in range(min(n, limit) + 1):
            # 剩余糖果数
            remain = n - i
            # 第二个人最少能分到的糖果数
            j_min = max(0, remain - limit)
            # 第二个人最多能分到的糖果数
            j_max = min(remain, limit)
            # 如果j的范围有效，则计算有效方案数
            if j_min <= j_max:
                count += j_max - j_min + 1
        return count
