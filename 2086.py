# %%
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if (
            "HHH" in hamsters
            or "." not in hamsters
            or hamsters[:2] == "HH"
            or hamsters[-2:] == "HH"
        ):
            return -1
        hamsters = hamsters.replace("H.H", "@")
        return hamsters.count("@") + hamsters.count("H")


a = Solution()
hamsters = ".H.H."
a.minimumBuckets(hamsters)
