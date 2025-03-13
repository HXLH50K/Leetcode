class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_valid_substring(s, k):
            vowels = set("aeiou")
            v_count = {v: 0 for v in vowels}
            c_count = 0

            # 统计元音和辅音
            for c in s:
                if c in vowels:
                    v_count[c] += 1
                else:
                    c_count += 1

            # 检查是否包含所有元音且恰好有k个辅音
            return all(v_count[v] > 0 for v in vowels) and c_count == k

        n = len(word)
        count = 0

        # 遍历所有可能的子串
        for i in range(n):
            for j in range(i + 5 + k, n + 1):  # 至少需要5个元音和k个辅音
                if is_valid_substring(word[i:j], k):
                    count += 1

        return count


# 测试代码
def test():
    s = Solution()

    # 测试用例1
    assert s.countOfSubstrings("aeioqq", 1) == 0

    # 测试用例2
    assert s.countOfSubstrings("aeiou", 0) == 1

    # 测试用例3
    assert s.countOfSubstrings("ieaouqqieaouqq", 1) == 3

    # 测试用例4
    assert s.countOfSubstrings("iqeaouqi", 2) == 3

    print("所有测试用例通过!")


if __name__ == "__main__":
    test()
