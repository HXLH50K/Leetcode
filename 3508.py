from collections import deque, defaultdict
from typing import List
import bisect


class Packet:
    """数据包对象，支持哈希与比较，便于去重。"""

    __slots__ = ("source", "destination", "timestamp")

    def __init__(self, source: int, destination: int, timestamp: int):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    def __hash__(self) -> int:
        return hash((self.source, self.destination, self.timestamp))

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Packet)
            and self.source == other.source
            and self.destination == other.destination
            and self.timestamp == other.timestamp
        )


class Router:
    """
    优化版 Router:
    - 使用 deque 存储按到达顺序的包 (source, destination, timestamp)，头删 O(1)。
    - 使用 set 去重，addPacket O(1) 判断重复。
    - 目的地 -> 有序时间戳列表，区间统计用二分 O(log k)。
    - 超出内存时淘汰最早包并同步更新结构。

    若需进一步降低删除时的 O(k)（列表中间 pop 引起移动）开销，可改为时间戳 -> 频次映射 + 单独的有序时间数组；此处保持易读实现。
    """

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        # 队列：按加入顺序保存 Packet
        self.queue = deque()
        # 去重集合 (Packet)
        self.seen = set()
        # 目的地 -> 排序时间戳列表（允许重复）
        self.dest_times = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """尝试加入数据包，重复返回 False。

        memoryLimit == 0 时：与原实现语义保持，直接返回 True（不存储）。
        """
        if self.memoryLimit == 0:
            return True

        packet = Packet(source, destination, timestamp)
        if packet in self.seen:
            return False

        # 若已满，淘汰最早
        if len(self.queue) == self.memoryLimit:
            old_packet = self.queue.popleft()
            self.seen.remove(old_packet)
            o_d = old_packet.destination
            o_t = old_packet.timestamp
            lst = self.dest_times[o_d]
            idx = bisect.bisect_left(lst, o_t)
            # 理论上一定找到
            if idx < len(lst) and lst[idx] == o_t:
                lst.pop(idx)
            if not lst:
                del self.dest_times[o_d]

        # 插入新包
        self.queue.append(packet)
        self.seen.add(packet)
        bisect.insort(self.dest_times[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        """转发（移除并返回最早的包），没有则返回 []。"""
        if not self.queue:
            return []
        pkt = self.queue.popleft()
        self.seen.remove(pkt)
        destination = pkt.destination
        timestamp = pkt.timestamp
        source = pkt.source
        lst = self.dest_times[destination]
        idx = bisect.bisect_left(lst, timestamp)
        if idx < len(lst) and lst[idx] == timestamp:
            lst.pop(idx)
        if not lst:
            del self.dest_times[destination]
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """统计当前缓存中指定目的地且时间戳在 [startTime, endTime] 的包数量。"""
        lst = self.dest_times.get(destination)
        if not lst:
            return 0
        left = bisect.bisect_left(lst, startTime)
        right = bisect.bisect_right(lst, endTime)
        return right - left
