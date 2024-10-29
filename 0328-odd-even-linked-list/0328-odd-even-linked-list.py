# Odd Even Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        temp1 = head
        temp2 = head.next
        temp3 = head.next
        i = 1
        
        while temp1 != None and temp2 != None:
            if temp2.next == None:
                break
            if i % 2 == 0:
                temp2.next = temp1.next
                temp2 = temp2.next
            elif i % 2 == 1:
                temp1.next = temp2.next
                temp1 = temp1.next
            i+=1
        temp1.next = temp3
        return head
                
            
