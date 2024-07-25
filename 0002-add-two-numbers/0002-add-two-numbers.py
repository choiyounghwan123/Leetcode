# Add Two Numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def toList(self, node: ListNode) -> list:
        list: list = []

        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self,result:str) -> ListNode:
        result = result[::-1]
        head:ListNode= ListNode(result[0])
        result1: ListNode = head
        for r in range(1,len(result)):
            node = ListNode(result[r])
            head.next = node
            head = head.next
        print(result)
        return result1


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(l1)
        b = self.toList(l2)
        resultStr = int("".join(str(e) for e in a[::-1])) + int("".join(str(e) for e in b[::-1]))

        return self.toReversedLinkedList(str(resultStr))
