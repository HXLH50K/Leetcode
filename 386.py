class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = list(range(1, n + 1))
        l.sort(key=lambda x: str(x))
        return l[:n]
