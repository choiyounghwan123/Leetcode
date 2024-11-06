# 706. Design HashMap
import collections


class ListNode:
    def __init__(self,key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index].key,self.table[index].value = key,value
            return

        p = self.table[index]

        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key,value)
        return
    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1

        p = self.table[index]

        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return
        
        if self.table[index].key is key:
            self.table[index] = self.table[index].next if self.table[index].next else ListNode()
            
        p = self.table[index]
        prev,p = p, p.next
        
        while p:
            if p.key == key:
                prev.next = p.next
                break
            prev ,p = p, p.next





# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)