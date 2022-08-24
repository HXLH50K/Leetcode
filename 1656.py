# %%
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [False] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey = idKey - 1
        assert not self.stream[idKey]
        self.stream[idKey] = value
        res = []
        while self.ptr < self.n and self.stream[self.ptr]:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)