class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0  # 记录连续空闲位置的数量
        start = 0  # 记录当前连续空闲空间的起始位置

        for i in range(len(self.mem)):
            if self.mem[i] == 0:  # 如果当前位置空闲
                if cnt == 0:  # 如果是新的空闲序列的开始
                    start = i
                cnt += 1
                if cnt == size:  # 找到足够大的空闲空间
                    # 分配内存
                    for j in range(start, start + size):
                        self.mem[j] = mID
                    return start
            else:  # 如果当前位置已被分配
                cnt = 0  # 重置计数器

        return -1  # 没有找到足够大的空闲空间

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                cnt += 1
        return cnt
