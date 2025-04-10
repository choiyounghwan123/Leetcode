# Reverse Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev:ListNode = None)->Optional[ListNode]:
            if not node:
                return prev
            
            next, node.next = node.next, prev
            return reverse(next,node)
        return reverse(head)