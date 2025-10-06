class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = dict()
        ans = [0] * len(rains)
        dry_days = []
        for i, r in enumerate(rains):
            if r == 0:
                dry_days.append(i)
            else:
                ans[i] = -1
                if r not in lakes:
                    lakes[r] = i  # lakes[r] filled at day i
                    continue

                if not dry_days:
                    return []  # no dry day to dry lake r
                # find the first dry day after lakes[r]
                for j in range(len(dry_days)):
                    if dry_days[j] > lakes[r]:
                        ans[dry_days.pop(j)] = r
                        lakes[r] = i
                        break
                else:
                    return []  # no dry day after lakes[r]

        while dry_days:
            ans[dry_days.pop()] = 1
        return ans
