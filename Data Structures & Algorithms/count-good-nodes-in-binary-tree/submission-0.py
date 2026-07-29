# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #o(n) time and space
        # requires a traversal, not a BST
        # probably want to recurse since we need information going bottom up
        # we have info on nodes from top down, on the way down
        # 2 -> 1 -> 3
        # either want a sorted DS or a way to store info that doesn't require it
        # for each value
        # maybe store a 'max so far'?
        # for each node, pass down a 'max so far' value
        # each node will return cumulative value of children (+ 1 if good)
        return self.countGoodNodes(root, -101)

    def countGoodNodes(self, node: TreeNode, maxSoFar: int) -> int:
        left = 0
        right = 0
        cur = 0

        # Get new max
        if node.val >= maxSoFar:
            maxSoFar = node.val
            cur = 1

        # Recurse
        if node.left:
            left = self.countGoodNodes(node.left, maxSoFar)
        if node.right:
            right = self.countGoodNodes(node.right, maxSoFar)

        # Return sum of all good nodes including this and below
        return left + right + cur

        # 2 - > 1 (1) -> 3 (1)
        # left = 1
        # right = 0
        # cur = 1
        # maxSoFar = 2


        # 2 1 3 5 8 2 3 9
        # 2 2 3 5 8 8 8 9
        # y x y y y x x y

        