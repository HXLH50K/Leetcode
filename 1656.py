# %%
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [False] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey = idKey - 1
        assert not self.stream[idKey]
        self.stream[idKey] = value


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)