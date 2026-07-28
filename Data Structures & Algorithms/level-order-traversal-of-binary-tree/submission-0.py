# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n) time and space
        # return level order traversal as nested list
        # is there a way to perform a level order traversal?
        # must be from left to right
        # maybe a queue? add all children to queue, then go to next item in queue
        # recurse with the height as an arg
        # then can just append to output[height]
        # maybe initialize list at bottom as base case
        output = []
        self.buildHeightMap(root, 0, output)
        return output
        
    def buildHeightMap(self, node, depth, levels):
        if node:
            # Add new level to list if necessary
            if depth == len(levels):
                levels.append([])
            
            # Build output from left to right across same-depth
            levels[depth].append(node.val)

            # Recurse
            if node.left:
                self.buildHeightMap(node.left, depth + 1, levels)
            if node.right:
                self.buildHeightMap(node.right, depth + 1, levels)

        
        