# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # only want T/F
        # given invariants directly here; just need to figure out ideal DS/algo
        # child nodes need parent node's val
        # entire left subtree needs to be smaller than node val
        # for each node, if left child is smaller than val
        # then left child's left children must be smaller than left child
        # and left childs' right children must be greater than left child but smaller than node
        # and vice versa for right
        # we want to set bounds; for every node there is a minimum and maximum value
        # for a left child, its max is current node, and min is same as prev
        # for a right child, its min is current node, and max is same as prev
        # need to worry about base case
        min = -1000000001
        max = 1000000001
        return self.validateBST(root, min, max)

    
    # For each node:
    #   Check that node's val falls between min and max, exclusive
    #   recurse on children with appropriate min and max as stated above
    #  
    #   Base case leaf node, validate node and return t/f
    #   Else return valid AND child valid
    def validateBST(self, node, min, max):
        # Validate current node
        if min < node.val < max:
            left = True
            right = True

            # Recurse
            if node.left:
                left = self.validateBST(node.left, min, node.val)
            if node.right:
                right = self.validateBST(node.right, node.val, max)
    
            # Only valid if both children valid
            return left and right
        else:
            return False
        


