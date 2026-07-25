# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # o(n) time and space (n = nodes in tree)
        # for every node, the left and right subtrees height must be within 1 unit of each other
        # e.g. abs(l - r) <= 1
        # return height and a bool
        # if bool is false, skip all other logic and pop back up and return
        # else
        # recurse on left and right children
        # compare their heights, and if acceptable, do nothing else set boolean to false
        # return current cumulative height
        return self.sameHeight(root)[1]
    
    def sameHeight(self, node) -> (int, bool):
        if node:
            # Recurse on children
            left = self.sameHeight(node.left)
            right = self.sameHeight(node.right)

            # If height not balanced, can stop tracking height and pop False up the chain
            if not (left[1] and right[1]):
                return (0, False)

            if abs(left[0] - right[0]) > 1:
                return (0, False)

            # Return height
            return (1 + max(left[0], right[0]), True)
        
        # Base case
        return (0, True)

