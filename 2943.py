from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        max_continuous_h_len = 0
        continuous_h_len = 1
        hBars.sort()
        for i in range(len(hBars) - 1):
            if hBars[i] + 1 == hBars[i + 1]:
                continuous_h_len += 1
            else:
                max_continuous_h_len = max(max_continuous_h_len, continuous_h_len)
                continuous_h_len = 1
        max_continuous_h_len = max(max_continuous_h_len, continuous_h_len)

        max_continuous_v_len = 0
        continuous_v_len = 1
        vBars.sort()
        for i in range(len(vBars) - 1):
            if vBars[i] + 1 == vBars[i + 1]:
                continuous_v_len += 1
            else:
                max_continuous_v_len = max(max_continuous_v_len, continuous_v_len)
                continuous_v_len = 1
        max_continuous_v_len = max(max_continuous_v_len, continuous_v_len)

        minn = min(max_continuous_h_len, max_continuous_v_len) + 1
        return minn * minn
