from typing import List


class Solution:
    def maximumBeauty(
        self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        flowers = [min(f, target) for f in flowers]
        flowers.sort()
        n = len(flowers)

        if flowers[0] == target:
            return n * full

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + flowers[i]

        res = 0
        j = n
        while j >= 0:
            if j < n:
                newFlowers -= max(0, target - flowers[j])
            if newFlowers < 0:
                break

            l, r = flowers[0], target - 1
            while l <= r:
                mid = (l + r) // 2
                idx = self.upper_bound(flowers, mid, 0, j)
                need = mid * idx - prefix[idx]
                if need <= newFlowers:
                    l = mid + 1
                else:
                    r = mid - 1

            min_partial = r if j > 0 else 0
            res = max(res, min_partial * partial + (n - j) * full)
            j -= 1

        return res

    def upper_bound(self, arr, val, left, right):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= val:
                left = mid + 1
            else:
                right = mid
        return left
