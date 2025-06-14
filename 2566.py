class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        first_non_zero_loc = next((i for i, c in enumerate(num_str) if c != "0"), None)
        first_non_zero_digit = (
            num_str[first_non_zero_loc] if first_non_zero_loc is not None else "0"
        )
        first_non_nine_loc = next((i for i, c in enumerate(num_str) if c != "9"), None)
        first_non_nine_digit = (
            num_str[first_non_nine_loc] if first_non_nine_loc is not None else "9"
        )
        min_num = num_str.replace(first_non_zero_digit, "0")
        max_num = num_str.replace(first_non_nine_digit, "9")
        return int(max_num) - int(min_num) if min_num and max_num else 0
