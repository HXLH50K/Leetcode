class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            n1 = list(map(int,list(str(n))))
            mul = 1
            for i in n1:
                mul *= i
            if mul % t == 0:
                return n
            n += 1