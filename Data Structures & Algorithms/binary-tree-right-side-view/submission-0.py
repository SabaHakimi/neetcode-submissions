# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # aim for O(n) time and space
        # how do we know a node is only visible from the right side of the tree?
        # the root obviously has nothing to its right
        # first intuition is the rightmost node at each height is the only node visible at that height
        # full traversal required?
        # can we simply traverse right-first and store one node per height level?
        # for each node, if it has a right child, go there. else go left
        # i think this guarantees seeing the visible node at each height first. so store first then process children
        # visible = [1, 3, 4, ]
        # node: 1 -> 2 -> 4 -> 5
        output = []
        if root:
            self.getVisibleNodes(root, 0, output)
        return output

    # Traverse and populate visible nodes
    # For each node:
    #   If visible list does not yet have an entry at this depth, expand list to accomodate new depth & add node val
    #   If node has right child, go there.
    #   If node has left child, go there.

    # only possible cases are len(arr) == depth or len(arr) > depth
    # only care to add new element if len(arr) = depth. otherwise, the rightmost node at that depth is already found
    def getVisibleNodes(self, node, depth, visible):
        # Update visible nodes
        if len(visible) == depth:
            visible.append(node.val)
        
        # Recurse
        if node.right:
            self.getVisibleNodes(node.right, depth + 1, visible)
        if node.left:
            self.getVisibleNodes(node.left, depth + 1, visible)
