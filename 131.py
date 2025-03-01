class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start: int, end: int) -> bool:
            # 判断子串是否为回文
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            # 如果起始位置已经到达字符串末尾，说明找到了一个分割方案
            if start >= len(s):
                res.append(path[:])
                return

            # 枚举所有可能的结束位置
            for end in range(start, len(s)):
                # 如果当前子串是回文串，继续往下搜索
                if isPalindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()  # 回溯，撤销选择

        res = []  # 存储所有分割方案
        backtrack(0, [])  # 从位置0开始回溯
        return res
