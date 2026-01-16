from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        hFences.sort()
        hFences.insert(0, 1)
        hFences.append(m)
        vFences.sort()
        vFences.insert(0, 1)
        vFences.append(n)

        h_diff = set()
        for i in range(len(hFences) - 1):
            for j in range(i + 1, len(hFences)):
                h_diff.add(hFences[j] - hFences[i])
        v_diff = set()
        for i in range(len(vFences) - 1):
            for j in range(i + 1, len(vFences)):
                v_diff.add(vFences[j] - vFences[i])
        union = h_diff & v_diff
        MOD = 10**9 + 7
        return (max(union) ** 2 % MOD) if union else -1
