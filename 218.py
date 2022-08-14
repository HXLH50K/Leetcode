# %%
class Solution:
    def getSkyline(self, buildings):
        buildings = sorted(buildings, key=lambda x: x[0])
        a = []
        for l, r, h in buildings:
            a.append((l, -h))
            a.append((r, h))
        a = sorted(a, key=lambda x: (x[0], x[1]))

        cur_handle = [0]  #如果是个空数组，max无法执行
        pre_max_height = 0
        cur_max_height = 0

        res = []

        for pos, height in a:
            if height < 0:
                cur_handle.append(-1 * height)
            else:
                cur_handle.remove(height)
            cur_max_height = max(cur_handle)
            if pre_max_height != cur_max_height:
                res.append([pos, cur_max_height])
                pre_max_height = cur_max_height

        return a


inputs = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
a = Solution()
print(a.getSkyline(inputs))
# %%
