from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given one node
        # return copy of graph
        # doesn't matter which node is returned?
        # need to deep copy:
        # value AND all neighbors
        # how to deep copy? cannot simply point to existing nodes, have to point to copy versions
        # 2 pass:
        # - 1st create all copies
        # - 2nd generate all relationships for copies
        # 
        # BFS through the graph:
        #   and for each node just create a copy node with val of original
        #   simultaneously populate hashmap with orig -> copy key val pairs (key & val are node itself)
        #   so that for 2nd pass, iterate keys in hashmap, and for every neighbor orig has,
        #   link up corresponding copy node to corresponding copy neighbors

        if not node:
            return None

        og_to_copy = {}

        # first pass BFS
        q = deque()
        visited = set()

        # load up queue with start node
        q.append(node)
        visited.add(node)

        while q:
            # process current
            current = q.popleft()
            # create copy and add to hashmap
            copy = Node(current.val)
            og_to_copy[current] = copy

            # explore neighbors
            for neighbor in current.neighbors:
                # if not visited, explore
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                

        # 2nd pass iterate map keys
        for og in og_to_copy:
            # for every neighbor the og node has,
            for neighbor in og.neighbors:
                copy = og_to_copy[og]
                copy_of_og_neighbor = og_to_copy[neighbor]
                copy.neighbors.append(copy_of_og_neighbor)

        # return any node in copy graph
        return og_to_copy[node]