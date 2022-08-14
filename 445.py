# %%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_a = []
        stack_b = []
        p = l1
        while p != None:
            stack_a.append(p.val)
            p = p.next
        p = l2
        while p != None:
            stack_b.append(p.val)
            p = p.next

        p = None
        flag = 0
        while stack_a != [] or stack_b != []:
            if stack_a != [] and stack_b != []:
                tmp = stack_a.pop() + stack_b.pop() + flag
            elif stack_a != []:
                tmp = stack_a.pop() + flag
            elif stack_b != []:
                tmp = stack_b.pop() + flag
            if tmp < 10:
                flag = 0
            else:
                tmp = tmp % 10
                flag = 1
            q = ListNode(tmp)
            q.next = p
            p = q
        if flag == 1:
            q = ListNode(1)
            q.next = p
            p = q
        return p


# %%
