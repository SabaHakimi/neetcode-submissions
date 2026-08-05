# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the two trees are the same if, for every node in t1, t2 has an identical node
        # traverse at the same time and compare every node
        # doesn't matter how we traverse
        return self.compareNodes(p, q)
        
    def compareNodes(self, p, q) -> bool:
        if p or q:
            if not (p and q and p.val == q.val):
                return False
            else:
                return self.compareNodes(p.left, q.left) and self.compareNodes(p.right, q.right)
        else:
            return True
            

