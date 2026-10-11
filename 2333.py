from typing import List
import heapq
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = []
        for a, b in zip(nums1, nums2):
            diff.append(abs(a - b))
        heap = [-d for d in diff]
        heapq.heapify(heap)
        k = k1 + k2
        while k > 0 and heap:
            largest = -heapq.heappop(heap)
            if largest == 0:
                break
            largest -= 1
            heapq.heappush(heap, -largest)
            k -= 1
        return sum(x * x for x in heap)