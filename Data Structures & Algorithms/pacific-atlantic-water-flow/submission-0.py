from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 2D array
        # each val is height (int)
        # 
        # top left is p and bottom right is a
        # water can flow in cardinal directions from each cell to neighbor with equal hiehgt or lower
        
        # return list of coords for all cells that can reach both oceans

        # work backwards from ocean (do this twice, have 2 sets for the 2 oceans)
        # for each ocean bordering tile:
            # mark visited
            # add to initial BFS queue and respective ocean set

        # BFS traversal
        # for every neighbor that has height equal or higher
        #   mark visited
        #   add to set and add to queue

        # for loop the pacific set:
        #   if element also in atlantic set, add to output

        reaches_pacific = self.getOceanSet(heights, 'pacific')
        reaches_atlantic = self.getOceanSet(heights, 'atlantic')
        reaches_both = []

        for coord in reaches_pacific:
            if coord in reaches_atlantic:
                reaches_both.append([coord[0], coord[1]])

        return reaches_both

    
                        
    def getOceanSet(self, heights, ocean):
        # Init vars
        q = deque()
        visited = set() # holds (r, c) tuples
        reach_ocean = set() # holds (r, c) tuples

        # what elements are bordering?
        # pacific -> first row and first col
        # atlantic -> last row and last col
        row_border_idx = 0
        col_border_idx = 0
        if ocean == 'atlantic':
            row_border_idx = len(heights) - 1
            col_border_idx = len(heights[0]) - 1

        for c in range(len(heights[0])):
            rc = (row_border_idx, c)
            visited.add(rc)
            q.append(rc)
            reach_ocean.add(rc)
        
        for r in range(len(heights)):
            rc = (r, col_border_idx)
            visited.add(rc)
            q.append(rc)
            reach_ocean.add(rc)

        # BFS exploration
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            current = q.popleft()
            r = current[0]
            c = current[1]

            # Explore all neighbors
            for neighbor in neighbors:
                # Calc neighbor coords
                dr = r + neighbor[0]
                dc = c + neighbor[1]
                rc = (dr, dc)

                if 0 <= dr < len(heights) and 0 <= dc < len(heights[0]) and rc not in visited:
                    # If neighbor equal height or greater
                    if heights[dr][dc] >= heights[r][c]:
                        # mark visited, add to queue, add to set
                        visited.add(rc)
                        q.append(rc)
                        reach_ocean.add(rc)

        return reach_ocean






