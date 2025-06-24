class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_locs = [i for i, num in enumerate(nums) if num == key]
        res = []
        for key_loc in key_locs:
            res.extend(range(max(0, key_loc - k), min(len(nums), key_loc + k + 1)))
        return sorted(set(res))
