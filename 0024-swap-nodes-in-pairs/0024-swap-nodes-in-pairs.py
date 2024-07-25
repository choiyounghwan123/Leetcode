# Swap Nodes in Pairs
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        root.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b
            prev = prev.next.next
            head = head.next
        return root.next