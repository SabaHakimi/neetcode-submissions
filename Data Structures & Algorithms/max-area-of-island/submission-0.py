from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # aiming to maximize a value
        # output int
        # input is 2D list/grid, only 0s or 1s, 1 is land 0 is water
        # OOB = 0/water
        # island consists of interconnected adjacent 1s in cardinal directions
        # area of island is numcells
        # search space is grid. 
        # naive approach: for each cell, explore until no longer possible
        # problem of duplicates!
        # it shold be the case that for any island, if you start exploring it from any point,
        # you will always explore the full island
        # only visit each island once -> only visit each node once
        # solution:
        # for each cell:
        #   if not already visited, run BFS
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_area = 0

        # For every cell in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == 0:
                    island_area = self.exploreIsland((row, col), grid, visited)
                    max_area = max(island_area, max_area)

        return max_area

    def exploreIsland(self, start, grid, visited):
        # BFS uses queue
        area = 0
        neighbors = deque()
        neighbors.append(start)

        while neighbors:
            # Process current
            current = neighbors.popleft()
            row = current[0]
            col = current[1]

            # Only process unvisited neighbors
            if visited[row][col] == 0:
                # Mark visited
                visited[row][col] = 1

                # Increase area and queue neighbors ONLY IF VALID CELL
                if grid[row][col] == 1:
                    area += 1

                    # Queue up neighbors
                    if len(grid) > row + 1:
                        neighbors.append((row + 1, col))
                    if len(grid[0]) > col + 1:
                        neighbors.append((row, col + 1))
                    if row > 0:
                        neighbors.append((row - 1, col))
                    if col > 0: 
                        neighbors.append((row, col - 1))
            
        return area








