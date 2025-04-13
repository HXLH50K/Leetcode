class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = sum(int(x) for x in s[:mid])
                right = sum(int(x) for x in s[mid:])
                if left == right:
                    cnt += 1
        return cnt
