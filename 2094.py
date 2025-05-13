from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # 使用Counter来统计每个数字出现的次数
        count = Counter(digits)
        result = set()

        # 遍历所有可能的三位数
        for i in range(100, 999, 2):  # 只考虑偶数
            # 将数字转换为字符串，以便于处理每一位
            num_str = str(i)
            # 统计当前数字中每个数字出现的次数
            curr_count = Counter(num_str)
            # 检查是否可以用digits中的数字构造出当前数字
            can_form = True
            for digit, freq in curr_count.items():
                if count[int(digit)] < freq:
                    can_form = False
                    break
            if can_form:
                result.add(i)

        # 转换为列表并排序
        return sorted(list(result))
