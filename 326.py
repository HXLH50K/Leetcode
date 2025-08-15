class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pows = [1]
        while True:
            pow_ = pows[-1] * 3
            if pow_ > 2**31 - 1:
                break
            pows.append(pow_)
        return n in pows
