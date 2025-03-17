class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0  # 用于统计未匹配的右括号数量
        max_unmatched = 0  # 记录最大未匹配右括号数量

        # 遍历字符串，统计未匹配的右括号
        for c in s:
            if c == "[":
                count -= 1
            else:  # c == ']'
                count += 1
            max_unmatched = max(max_unmatched, count)

        # 需要交换的次数就是 (max_unmatched + 1) // 2
        # 因为每次交换可以减少2个未匹配的右括号
        return (max_unmatched + 1) // 2
