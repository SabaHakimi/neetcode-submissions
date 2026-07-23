"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(n) time & space
        # can't just iterate the ll because of random pointer
        # need to be able to copy the random node in its relation to the other nodes, for each node
        #   for each node, 
        #       need to be able to get random node's attributes (access via node.random.x)
        #       need to be able to assign the current node's random to be that node with those attributes
        # what is the problem with rand? for each respective node in original, need to point to that same node in copy
        # dict? 2 pass
        # add all keys first
        # then via dict we will have access to other nodes references
        # idea is dict[Node1] holds copy of node1
        # and so value is just dict[Node1].value
        # next is dict[dict[Node1].next]
        # random is dict[dict[Node1].random]

        # Base case
        if not head:
            return None
            
        # Original Node -> Copy Node
        copies = {}

        # Populate dict with only keys and empty copy first (each original node is a key)
        cur = head
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        # Populate copy references
        cur = head
        while cur:
            # Base case, could be None
            next_copy = None
            next_random = None
            
            # Find corresponding copy nodes of original refs
            if cur.next in copies:
                next_copy = copies[cur.next]
            if cur.random in copies:
                next_random = copies[cur.random]

            # Assign copies
            copies[cur].next = next_copy
            copies[cur].random = next_random

            # Proceed
            cur = cur.next

        # Return head of copied list
        return copies[head]

        # (3, None) -> (7, 5) -> (4, 3) -> (5, 7) -> Null

        # copies = {
        #     (3, None): (3, None)
        #     (7, 5):    (7, None)
        #     (4, 3):    (4, None)
        #     (5, 7):    (5, None)
        # }
        # cur = (7, 5)
        # next_copy = (7, None)
        # next_random = (None)

    