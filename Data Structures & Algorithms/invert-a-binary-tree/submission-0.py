# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # seems like recursion
        # while you have a left and a right:
        #   recurse
        #   then from bottom up:
        #   swap left child with right child
        if root:
            self.invert(root)
        return root

    def invert(self, current):
        # Recurse
        if current.left:
            self.invert(current.left)
        if current.right:
            self.invert(current.right)
        
        temp = current.left
        current.left = current.right
        current.right = temp
