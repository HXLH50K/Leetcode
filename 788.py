class Solution:
    def is_good(self, num: int) -> bool:
        has_good_digit = False

        for c in str(num):
            if c in ['3', '4', '7']:
                return False
            elif c in ['2', '5', '6', '9']:
                has_good_digit = True
        return has_good_digit

    def rotatedDigits(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            if self.is_good(i):
                count += 1

        return count