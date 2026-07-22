# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Locate target distance from EOL
        i = 0
        scout = head
        while scout.next is not None:
            scout = scout.next
            i += 1
        target = i - n
        
        # If removing first element
        if target == -1:
            return head.next
        
        # Locate target
        pre_target = head
        for i in range(target):
            pre_target = pre_target.next
        
        # Remove target
        pre_target.next = pre_target.next.next

        
        return head