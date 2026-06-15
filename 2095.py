# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        prev = None
        while fast:
            fast = fast.next
            if not fast:
                prev.next = slow.next
                return head
            prev = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                prev.next = slow.next
                return head
        return head