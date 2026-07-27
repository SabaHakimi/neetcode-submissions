# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # aim for O(h) time and space where h = height of tree
        # the challenge here is in that you have to both find the values and determine a common ancestor
        # what information can we acquire after traversing to the nodes?
        # we know that all node values are unique
        # if we store a dict for one node's path up, we can then check at every point on the second node's journey up
        # if a given node is within the visited dict of the previous node. 

        # Traverse to p and build visited set; guaranteed to find p
        visited = {p.val}
        cur_node = root
        while cur_node.val != p.val:
            visited.add(cur_node.val)
            if p.val < cur_node.val:
                cur_node = cur_node.left
            elif p.val > cur_node.val:
                cur_node = cur_node.right
        
        return self.findFirstAncestor(root, q, visited)
    
    def findFirstAncestor(self, cur, q, visited):
        # Recurse until q
        ancestor = None
        if cur.val != q.val:
            if q.val < cur.val:
                ancestor = self.findFirstAncestor(cur.left, q, visited)
            elif q.val > cur.val:
                ancestor = self.findFirstAncestor(cur.right, q, visited)
        
        # If ancestor found, return up the chain
        if ancestor:
            return ancestor
        elif cur.val in visited:
            return cur
        else:
            return None
        



