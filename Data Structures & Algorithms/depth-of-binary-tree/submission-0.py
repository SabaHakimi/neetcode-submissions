# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for each branch, recurse (until hit bottom)
        # return 1 at bottom, then 1 + current tally otherwise
        # always take the max of your two children. this guarantees max depth when returning to root
        if root is not None:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
        else:
            return 0
        
        return 1 + max(l_depth, r_depth)