from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # don't know where cells are relative to chest -> BFS
        # modify grid in-place
        # search space? overwrite land cells 
        # objective is treasure chests -> search on chests; run multi-source BFS
        # multi-source because 'nearest' chest
        # when BFS-ing and going through neighbors"
        # - can't be water
        # - can't already be visited
        # - need to track distance? current node val + 1 to neighbors
        
        visited = set()
        q = deque()

        # Traverse grid, queue all chests for a BFS
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If chest, queue for BFS
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        # BFS
        while q:
            # Get current node
            current = q.popleft()
            row = current[0]
            col = current[1]

            # Get neighbors
            neighbors = [
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1)
            ]

            # Explore neighbors
            for r, c in neighbors:
                # Check in bounds
                if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                    # Set distance, mark visisted, and queue up if not water and not visited
                    if grid[r][c] != -1 and (r, c) not in visited:
                        # Distance to chest is one greater than the current node's distance to chest
                        grid[r][c] = grid[row][col] + 1
                        visited.add((r, c))
                        q.append((r, c))



