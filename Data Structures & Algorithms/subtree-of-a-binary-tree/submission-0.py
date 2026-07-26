# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # aim for O(m * n) time and O(m + n) space
        # for every node check if it could be the subtree
        # create a helper that takes two nodes and verifies if they are the same tree
        # then for each node in main tree, call that helper with the subtree root

        # how to determine if two trees are the same tree:
        # for each node in t1, t1 must have a corresponding identical node
        # invariant: [t1 and t2 exists, t1 and t2 have same value], and have identical children (recurse on children)

        return self.traverseTree(root, subRoot)

    # For every node in the tree, if sameTree returns True, return True up the chain
    def traverseTree(self, t1, t2) -> bool:
        if self.sameTree(t1, t2):
            return True
        
        left = False
        right = False
        if t1.left:
            left = self.traverseTree(t1.left, t2)
        if t1.right:
            right = self.traverseTree(t1.right, t2)
        
        return left or right
            
    

    def sameTree(self, t1, t2) -> bool:
        if t1 or t2:
            # Check node equality
            if t1 and t2 and t1.val == t2.val:
                # Recurse on children even if they don't exist
                left = self.sameTree(t1.left, t2.left)
                right = self.sameTree(t1.right, t2.right)
                return left and right
            else:
                return False
        # If both don't exist
        else:
            return True
    