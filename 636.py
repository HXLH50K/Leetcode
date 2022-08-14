# %%
from typing import List
from collections import defaultdict


class Solution:

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = defaultdict(int)
        stack = []
        for log in logs:
            id_, status, t = log.split(":")
            id_ = int(id_)
            t = int(t)
            if not stack:
                assert status == "start"
                stack.append((id_, status, t))
                continue    
            last_id, last_status, last_t = stack[-1]
            if id_ == last_id and status == "end" and last_status == "start":
                times[id_] += t - last_t + 1 - stop_time
                stop_time += times[id_]
                stack.pop()
            else:
                stack.append((id_, status, t))
        return times


a = Solution()
n = 1
logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
a.exclusiveTime(n, logs)
# %%
