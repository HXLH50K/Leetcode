# %%
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        a = {}
        p = head
        while p != None:
            a[p] = Node(p.val)
            p = p.next
        p = head
        while p != None:
            if p.next:
                a[p].next = a[p.next]
            else:
                a[p].next = None
            if p.random:
                a[p].random = a[p.random]
            else:
                a[p].random = None
            p = p.next
        return a[head]


a = Solution()
a.copyRandomList(b)
