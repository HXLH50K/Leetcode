# %%
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        import numpy as np
        customers = np.array(customers)
        grumpy = np.array(grumpy)
        a = customers * (1 - grumpy) # 不发动技能满意的人
        b = customers * grumpy # 不满意的
        sat_cus = a.sum()
        sub_sat = temp = sum(b[0:X])
        for i in range(1, len(a) - X + 1):
            temp -= b[i-1]
            temp += b[i+X-1]
            sub_sat = max(sub_sat, temp)
        return sat_cus + sub_sat

def main():
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    X = 3
    ret = Solution().maxSatisfied(customers, grumpy, X)
    out = str(ret)
    print(out)

if __name__ == '__main__':
    main()
# %%
