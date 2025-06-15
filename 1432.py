class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        first_non_zero_loc = next((i for i, c in enumerate(num_str) if c != "0"), 0)
        first_non_zero_digit = (
            num_str[first_non_zero_loc] if first_non_zero_loc is not None else "0"
        )
        first_more_one_loc = next(
            (i for i, c in enumerate(num_str) if c not in "01"), 0
        )
        first_more_one_digit = (
            num_str[first_more_one_loc] if first_more_one_loc is not None else "1"
        )
        first_non_nine_loc = next((i for i, c in enumerate(num_str) if c != "9"), 0)
        first_non_nine_digit = (
            num_str[first_non_nine_loc] if first_non_nine_loc is not None else "9"
        )
        if first_more_one_loc != 0:  # 123 -> 103
            min_num = num_str.replace(first_more_one_digit, "0")
        else:  # 234 -> 134
            min_num = num_str.replace(first_non_zero_digit, "1")
        max_num = num_str.replace(first_non_nine_digit, "9")
        return int(max_num) - int(min_num) if min_num and max_num else 0
