class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        for i, row in enumerate(mat):
            cnt = row.count(1)
            if cnt > ans[1]:
                ans = [i, cnt]
        return ans
