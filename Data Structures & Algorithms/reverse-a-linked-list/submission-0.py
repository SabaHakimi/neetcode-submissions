# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while (cur is not None):
            stack.append(cur)
            cur = cur.next
        if len(stack) == 0:
            return

        new_head = ListNode(stack.pop().val)
        node = new_head
        while len(stack) > 0:
            popped = stack.pop()
            node.next = popped
            node = node.next
        node.next = None

        return new_head
        # Iterate list, add each item to stack
        # Pop pop pop