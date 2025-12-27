from typing import List
import heapq


class Meeting:
    def __init__(self, start: int, end: int):
        self.ori_start = start
        self.ori_end = end
        self.duration = end - start
        self.actual_start = None
        self.actual_end = None

    def __lt__(self, other):
        # sort by ori_start only
        return self.ori_start < other.ori_start


class Room:
    def __init__(self, idx: int):
        self.idx = idx
        self.next_free_time = 0
        self.meeting_count = 0

    def __lt__(self, other):
        # sort by next_free_time, then by idx
        if self.next_free_time == other.next_free_time:
            return self.idx < other.idx
        return self.next_free_time < other.next_free_time


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings_objs = sorted([Meeting(start, end) for start, end in meetings])

        # available_rooms stores Room objects, sorted by idx because next_free_time is 0
        available_rooms = [Room(i) for i in range(n)]
        heapq.heapify(available_rooms)

        # occupied_rooms stores Room objects, sorted by next_free_time
        occupied_rooms = []

        for meeting in meetings_objs:
            # Free up rooms that are now available
            while (
                occupied_rooms and occupied_rooms[0].next_free_time <= meeting.ori_start
            ):
                room = heapq.heappop(occupied_rooms)
                # Reset next_free_time so that __lt__ sorts by idx in available_rooms
                room.next_free_time = 0
                heapq.heappush(available_rooms, room)

            if available_rooms:
                # Assign to the available room with the smallest index
                room = heapq.heappop(available_rooms)

                room.meeting_count += 1
                room.next_free_time = meeting.ori_start + meeting.duration

                heapq.heappush(occupied_rooms, room)
            else:
                # Delay the meeting, use the room that frees up earliest
                room = heapq.heappop(occupied_rooms)

                room.meeting_count += 1
                room.next_free_time += meeting.duration

                heapq.heappush(occupied_rooms, room)

        # Collect all rooms to find the one with the most bookings
        all_rooms = available_rooms + occupied_rooms

        # Sort by meeting_count (desc) and then idx (asc)
        all_rooms.sort(key=lambda r: (-r.meeting_count, r.idx))

        return all_rooms[0].idx
