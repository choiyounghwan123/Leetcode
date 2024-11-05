# 622 Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxLen = k
        self.q1 = 0
        self.q2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.q2] is None:
            self.q[self.q2] = value
            self.q2 = (self.q2 + 1) % self.maxLen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.q1] is not None:
            self.q[self.q1] = None
            self.q1 = (self.q1 + 1) % self.maxLen
            return True
        else:
            return False
    def Front(self) -> int:
        return -1 if self.q[self.q1] is None else self.q[self.q1]

    def Rear(self) -> int:
        return -1 if self.q[self.q2-1] is None else self.q[self.q2-1]

    def isEmpty(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is None
    def isFull(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q2] is not None

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(7))
# param_2 = obj.deQueue()
print(obj.Front())
print(obj.deQueue())
print(obj.Front())
print(obj.Rear())
print(obj.enQueue(0))
print(obj.isFull())
print(obj.deQueue())
print(obj.Rear())
print(obj.enQueue(3))



# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
