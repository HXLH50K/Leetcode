class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        left = k // 2 + 1
        ans = 0
        if left > n:
            return sum(range(1, n + 1))
        cnt = 0
        i = 1
        while cnt < n:
            if i < left or i > k - 1:
                ans += i
                i += 1
                cnt += 1
            else:
                i += 1
        return ans
