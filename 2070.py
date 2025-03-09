from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # 按价格排序
        items.sort()
        prices = []
        max_beauty = []
        curr_max = 0

        # 只保留每个价格点的最大美丽值
        for price, beauty in items:
            if not prices or price != prices[-1]:
                prices.append(price)
                curr_max = max(curr_max, beauty)
                max_beauty.append(curr_max)
            else:
                max_beauty[-1] = max(max_beauty[-1], beauty)
                curr_max = max(curr_max, beauty)

        ans = []
        for q in queries:
            # 二分查找小于等于q的最大价格点
            i = bisect_right(prices, q)
            if i == 0:  # 没有找到符合条件的价格点
                ans.append(0)
            else:
                ans.append(max_beauty[i - 1])

        return ans
