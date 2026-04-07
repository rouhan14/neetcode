# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        p1 = l1
        p2 = l2
        rem = 0

        while p1 and p2:
            curr.next = ListNode((p1.val + p2.val + rem)%10)
            rem = (p1.val + p2.val + rem)//10

            curr = curr.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            curr.next = ListNode((p1.val + rem)%10)
            rem = (p1.val + rem)//10

            curr = curr.next
            p1 = p1.next

        while p2:
            curr.next = ListNode((p2.val + rem)%10)
            rem = (p2.val + rem)//10

            curr = curr.next
            p2 = p2.next
        
        if rem != 0:
            curr.next = ListNode(rem)

        return dummy.next




