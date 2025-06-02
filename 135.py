class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                res.append(res[-1] + 1)
            else:
                res.append(1)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        return sum(res)
