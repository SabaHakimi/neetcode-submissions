# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # aim for O(m + n) time, O(1) space
        # not creating a list of new node objects, reuse
        # lots of edge cases here?
        # basic case is just add l1 and l2 vals, assign to l1, then increment both pointers
        # need to worry about carrying the one
        # also need to worry about one list being empty
        # more generally:
        # for each node
        #   there are 2 values that need to be assigned to a node, and pointers need to be incremented

        # For each node, add values, if needed carry the one, then increment to next node
        
        if not l1:
            l1 = l2
            l2 = None
        
        head = l1

        while l1:
            # Retrieve operands        
            op1 = l1.val
            op2 = 0

            if l2:
                op2 = l2.val

            sum = op1 + op2
            if sum > 9:
                # Carry the one
                sum %= 10
                
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)

            # Assign new val
            l1.val = sum
            
            # Increment
            # If l1 ends early, just make l2 become the new l1
            if not l1.next and l2 and l2.next:
                l1.next = l2.next
                l1 = l2.next
                l2 = None
            else:
                l1 = l1.next
                if l2:
                    l2 = l2.next

        return head


