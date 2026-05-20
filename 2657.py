from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_A = set()
        set_B = set()
        n = len(A)
        C = [0] * n
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            C[i] = len(set_A & set_B)
        return C