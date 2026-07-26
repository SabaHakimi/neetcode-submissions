# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # aim for O(n) time and space
        # i think we can just do a tree traversal and compare equality at every step, then return true
        # false otherwise
        # invariant: if for every node in t1, t2 has an identical equivalent node, they are equal
        # maybe handle base case in main func
        if p and q:
            return self.traverseTrees(p, q)
        elif p and not q:
            return False
        elif q and not p:
            return False
        else:
            return True
    
    # For each node compare value across trees, then explore all children
    def traverseTrees(self, t1, t2):
        # Compare values
        if t1.val != t2.val:
            return False

        # Recurse
        if t1.left or t2.left:
            if t1.left and t2.left:
                left = self.traverseTrees(t1.left, t2.left)
                if not left:
                    return False
            else:
                return False
        
        if t1.right or t2.right:
            if t1.right and t2.right:
                right = self.traverseTrees(t1.right, t2.right)
                if not right:
                    return False
            else:
                return False
        
        return True
        
