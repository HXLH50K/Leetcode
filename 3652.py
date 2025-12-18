# %%
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original_profit = 0
        n = len(prices)
        for i in range(n):
            original_profit += prices[i] * strategy[i]

        original_profit_windows = [sum([strategy[j] * prices[j] for j in range(k)])]
        for i in range(k, n):
            now_window_profit = (
                original_profit_windows[-1]
                - strategy[i - k] * prices[i - k]
                + strategy[i] * prices[i]
            )
            original_profit_windows.append(now_window_profit)
        new_profit_windows = [sum(prices[j] for j in range(k // 2, k))]
        for i in range(k, n):
            now_window_profit = (
                new_profit_windows[-1] - prices[i - k + k // 2] + prices[i]
            )
            new_profit_windows.append(now_window_profit)

        max_profit = original_profit
        for i in range(len(original_profit_windows)):
            max_profit = max(
                max_profit,
                original_profit - original_profit_windows[i] + new_profit_windows[i],
            )
        return max_profit


prices = [4, 7, 13]
strategy = [-1, -1, 0]
k = 2
Solution().maxProfit(prices, strategy, k)

# %%
