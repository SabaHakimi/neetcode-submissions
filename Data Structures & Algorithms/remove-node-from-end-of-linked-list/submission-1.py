# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) time O(1) space
        # could potentially reverse, remove element, re-reverse OR
        # iterate once to get size of list
        # remove nth node
        # return head
       
        # Solution

        # Get count
        count = 1
        cur = head
        while cur.next:
            cur = cur.next
            count += 1

        # Calc idx for element to remove
        idx = count - n

        # Base case
        if idx == 0:
            return head.next

        # Traverse to element
        cur = head
        i = 0
        while i < idx - 1:
            cur = cur.next
            i += 1

        # Remove next element
        if cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        return head


        # 1 2 3 4
        # count = 4
        # idx = 2

        # cur = 2 > 4
        # i = 1


        
        