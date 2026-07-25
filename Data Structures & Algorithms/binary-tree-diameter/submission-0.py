# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # want O(n) time and O(n) space, n = num nodes in tree
        # find longest path between any two nodes in tree
        # length defined by num edges between nodes
        # cannot include same node twice
        # figure out how to get longest path
        # leaning towards using recursion to get the cumulative length (bottom up) for any given node
        # track the maximum and return it
        # need to determine invariant for what defines the length of a path for a given node
        # for each node:
        # base case path length is 0 for a leaf node
        # a node's evaluated path length for contention as the maximum is the combined length of its left and right child paths
        # the length a node returns to its parent is 1 + the maximum of its two children's lengths
        return self.findMaxPath(root)[1]
    
    # Returns tuple in format of (path_len, max_path_found)
    def findMaxPath(self, node):
        if node.left or node.right:
            # Recurse
            left = (0, 0)
            right = (0, 0)
            if node.left:
                left = self.findMaxPath(node.left)
            if node.right:
                right = self.findMaxPath(node.right)

            # Get max path len between len of two children and max lens found on either child branch
            max_len = max(left[0] + right[0], left[1], right[1])
            return (1 + max(left[0], right[0]), max_len)
        # If leaf
        else:
            return (1, 0)

    # fMP(1) -> fMP(2) -> fMP(3) -> fMP(5) returns (0, 0)
    # fMP(1) -> fMP(2) -> fMP(3) returns (2, 1)
    # fMP(1) -> fMP(2) -> fMP(4) returns (1, 0)
    # fMP(1) -> fMP(2) returns (3, 3)
    # fMP(1) returns (4, 3)



