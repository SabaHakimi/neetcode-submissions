# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #O(n) time O(1) space
        # for every element, its next attribute should point to the element who's next currently points to it
        # for each element:
        #   track current as prev for next element
        #   store existing next as temp to process next
        #   set next to prev
        cur = head
        prev = None

        while cur is not None:
            # preserve next
            next = cur.next

            # reverse this element's next
            cur.next = prev

            # return if done
            if next is None:
                return cur

            # have prev ready for next element
            prev = cur
            
            # update cur
            cur = next




    #     [0,1,2,3]

    #    None <- 0 <- 1 <- 2 <- 3 -> None
    #     cur = None
    #     next = None
    #     prev = (3)
