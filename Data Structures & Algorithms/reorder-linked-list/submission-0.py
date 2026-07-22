# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first, last, second, second to last
        # what's the pattern here
        # 1 2 3 4 5 6 -> 1 6 2 5 3 4
        # o(n) time o(1) space -> build new list in place/rewrite existing list
        # alternating elements from left to right and right to left
        # first half is simple
        # how to get elements from end of the list in reverse order?
        # reverse second half of the list
        # after reversing, simply alternate between elements in first half and elements in reversed second half

        # Reverse second half of the list

        # Get to second half
        # 1, 2 -> 1, 2

        # 1, 2, 3 -> 1, 3, 2

        # 1, 2, 3, 4 -> 1, 4, 2, 3

        # either first element of second half (even)
        # first element after middle element (odd)

        # how?

        # Find starting point of second half of the list
        slow = head
        fast = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        # Severe two halves
        prev.next = None

        # Reverse second half of the list
        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Build output alternating elements
        l1 = head
        l2 = prev

        while l2:
            # alternate references
            l1_next = l1.next
            l1.next = l2
            l1 = l1_next

            l2_next = l2.next
            l2.next = l1
            l2 = l2_next

        # 1 -> 2 and 4 -> 3

        # 1 -> 4 -> 2 -> 3 -> None

        # 1 -> 5 -> 2 -> 4 -> 3 -> None

        # 1 -> 2 -> 3  and 5 -> 4 -> None

        # 1 -> 5 -> 2 -> 4 -> 4
        


        