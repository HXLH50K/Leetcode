class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:  # If length is odd, it can't be valid
            return False

        def check(s: str, locked: str, bracket: str) -> bool:
            balance = 0  # Track bracket balance
            free = 0  # Count of unlocked positions

            # If bracket is ')', we scan right to left and check closing brackets
            # If bracket is '(', we scan left to right and check opening brackets
            range_to_check = (
                range(len(s)) if bracket == "(" else range(len(s) - 1, -1, -1)
            )

            for i in range_to_check:
                if locked[i] == "1":
                    balance += 1 if s[i] == bracket else -1
                else:
                    free += 1

                # At any point, we can use our free positions to fix the balance
                # but balance + free must be >= 0 to have enough positions to fix
                if balance + free < 0:
                    return False

            # Final check: can we achieve valid balance using free positions?
            return balance <= free and (balance + free) % 2 == 0

        # Check both directions:
        # 1. Left to right ensuring we have enough opening brackets
        # 2. Right to left ensuring we have enough closing brackets
        return check(s, locked, "(") and check(s, locked, ")")
