# %%
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        new_events = []
        for event in events:
            event_type, timestamp, event_op = event
            timestamp = int(timestamp)
            if event_type == "OFFLINE":
                user_id = int(event_op)
                new_events.append(["ONLINE", timestamp + 60, user_id])
                new_events.append(["OFFLINE", timestamp, user_id])
            elif event_type == "MESSAGE":
                mentions_string = event_op
                if mentions_string in ["HERE", "ALL"]:
                    new_events.append(["MESSAGE", timestamp, mentions_string])
                    continue
                mentions = mentions_string.split(" ")
                mentions = [int(uid[2:]) for uid in mentions]
                new_events.append(["MESSAGE", timestamp, mentions])

        events = new_events
        events.sort(
            key=lambda x: (x[1], {"OFFLINE": 1, "ONLINE": 0, "MESSAGE": 2}[x[0]])
        )

        online_users = set(range(numberOfUsers))
        mentions_count = [0] * numberOfUsers
        for event in events:
            event_type, _, event_op = event
            if event_type == "ONLINE":
                online_users.add(event_op)
            if event_type == "OFFLINE":
                online_users.remove(event_op)
            if event_type == "MESSAGE":
                mentions_string = event_op
                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions_count[i] += 1
                elif mentions_string == "HERE":
                    for user_id in online_users:
                        mentions_count[user_id] += 1
                else:
                    for user_id in mentions_string:
                        mentions_count[user_id] += 1
        return mentions_count


numberOfUsers = 2
events = [
    ["MESSAGE", "10", "id1 id0"],
    ["OFFLINE", "11", "0"],
    ["MESSAGE", "12", "ALL"],
]
solution = Solution()
print(solution.countMentions(numberOfUsers, events))  # Output: [2,

# %%
