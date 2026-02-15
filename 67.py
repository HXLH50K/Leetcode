class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a
        b = "0b" + b
        a = int(a, 2)
        b = int(b, 2)
        c = a + b
        c = bin(c)
        return c[2:]
