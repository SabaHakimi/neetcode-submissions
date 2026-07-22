# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # want O(n + m) time, O(1) space
        # not building a new list of objects b/c O(1) space
        # new chain of pointers; rewrite .next vals, and as you do, set each node to be its .next
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next

        while list1:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        
        while list2:
            tail.next = list2
            tail = tail.next
            list2 = list2.next

        return dummy.next
        
        # 5
        # 0 - 1 - 1 - 2 - 3 - 4 
