# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num_visited = 0
        # bst, so we have sorted order
        # given root
        # search space is values within tree, bounded by smallest and largest vals
        # get kth smallest
        # how do we find an kth smallest value?
        # there is probably a way to find this within the tree, without additional DS
        # O(n) time, O(n) space
        # because bst
        # for each node, the left subtree is smaller than it, and right subtree is greater
        # pre order traversal, keep track of k
        return self.preorderTraverse(root, k)

    # preorder traverse
    # for each node
    # go left first
    # process current -> mark as visited, if at k return val, else None
    # go right after
    def preorderTraverse(self, node, k):
        # Process left
        if node.left:
            left = self.preorderTraverse(node.left, k)
            # If kth smallest found, return it
            if left is not None:
                return left
        
        # Process current
        self.num_visited += 1
        if self.num_visited == k:
            return node.val

        # Process right
        if node.right:
            right = self.preorderTraverse(node.right, k)
            # If kth smallest found, return it
            if right is not None:
                return right



        