class Solution:
    def secondHighest(self, s: str) -> int:
        flag = False
        for i in range(9, -1, -1):
            if str(i) in s:
                if not flag:
                    flag = True
                else:
                    return i
        return -1
