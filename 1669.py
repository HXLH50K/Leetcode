# %%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        head = p = list1
        i = 0
        while i < a - 1:
            i += 1
            p = p.next
        start = p
        while i < b:
            i += 1
            p = p.next
        end = p.next
        p = list2
        while p.next:
            p = p.next
        p.next = end
        start.next = list2
        return head
