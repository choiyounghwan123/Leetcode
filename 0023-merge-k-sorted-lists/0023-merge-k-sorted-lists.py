# 23. Merged k Sorted Lists

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap,(result.next.val,idx,result.next))

        return root.next


a1 = ListNode(1)
a1.next = ListNode(4)
a1.next.next = ListNode(5)
a2 = ListNode(1)
a2.next = ListNode(3)
a2.next.next = ListNode(4)
a3 = ListNode(2)
a3.next = ListNode(6)
lists = [a1, a2, a3]
print(Solution().mergeKLists([[]]))
