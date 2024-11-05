# 641. Design Circular Deque

class ListNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        n.left, new.right = new, n
        new.left = node

    def _del(self,node:ListNode):
        n = node.right.right
        node.right = node.right.right
        n.left = node


    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len != 0:
            self._del(self.head)
            self.len -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.len == 0 else self.head.right.val

    def getRear(self) -> int:
        return -1 if self.len == 0 else self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
