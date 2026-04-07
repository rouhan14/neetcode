# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Finding middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now the slow pointer is in exact half
        # Reverse the second half

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Now the second half has been reversed
        p1 = head
        p2 = prev

        while p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1

            p1 = tmp1
            p2 = tmp2
