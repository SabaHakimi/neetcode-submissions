# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first thought is it's good that lists are backwards, can just add em digit by digit
        # want O(m + n) time and O(1) space; process each element once, don't create a new list with m + n objs
        # edge cases? complexities?
        # want to carry the 1 if needed; both lists have at least one element for base case
        # since one list can be shorter, should probably have a tail node
        
        tail = ListNode()
        head = tail
        carry = 0

        while l1 or l2 or carry:
            # Get ops
            operand1 = 0
            operand2 = 0

            if l1:
                operand1 = l1.val
            if l2:
                operand2 = l2.val

            # Calc sum & carryover
            sum = operand1 + operand2 + carry
            
            if sum >= 10:
                sum %= 10
                carry = 1
            else:
                carry = 0

            # if either list exists assign that node to be the next node and reassign it's value
            nxt = None
            if l1:
                nxt = l1
                l1.val = sum
                l1 = l1.next
            if l2:
                nxt = l2
                l2.val = sum
                l2 = l2.next
            
            # assign next, or create if necessary
            if nxt:
                tail.next = nxt
                tail = tail.next
            elif sum:
                tail.next = ListNode(1)


        return head.next
            

        # op1 = 9
        # op2 = 9
        # sum = 8
        # carry = 1
        # nxt = (0)

        # head: 0 1 1

        # 9 9 
        # 1 1

        # 0 >9
        # 0 >1

        


        