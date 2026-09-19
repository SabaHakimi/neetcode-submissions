from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # counting 'ticks'
        # 3 possible values per cell
        # neighbors in cardinal directions rot each tick
        # what happens when u BFS ?
        # need to run multiple simultaneous BFS
        # how to figure out when all vals rotten?
        # OR the tick upon which all vals finally rotted
        # track current tick + tick of last rot
        # pass the tick count with neighbor
        # need to know if there are any unrotted fruit by the end, so should count all fresh fruit on 1st pass
        
        # Count fresh fruit
        num_fresh_fruit = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    num_fresh_fruit += 1

        

        # Queue up rotters (row, col, tick)
        q = deque()
        
        # Track via index pair tuples (row, col)
        visited = set()

        # Iterate over entire 2D array, queue up all rotted fruit simultaneously into a BFS
        # Track 'generations/ticks' for new neighbors
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Mark rotters visited and add to queue
                if grid[row][col] == 2:
                    visited.add((row, col))
                    q.append((row, col, 0))
        
        tick = 0
        # BFS until all rotters have fully extended their spread or no fresh fruit left
        while q and num_fresh_fruit > 0:
            # Get current
            current = q.popleft()
            row = current[0]
            col = current[1]
            tick = current[2]

            # Queue neighbors in cardinal directions and mark visited
            # Ensure within bounds, not visited, and not an empty space
            if row < len(grid) - 1 and (row + 1, col) not in visited and grid[row + 1][col] != 0:
                visited.add((row + 1, col))
                q.append((row + 1, col, tick + 1))
                num_fresh_fruit -= 1
            if col < len(grid[0]) - 1 and (row, col + 1) not in visited and grid[row][col + 1] != 0:
                visited.add((row, col + 1))
                q.append((row, col + 1, tick + 1))
                num_fresh_fruit -= 1
            if row > 0 and (row - 1, col) not in visited and grid[row - 1][col] != 0:
                visited.add((row - 1, col))
                q.append((row - 1, col, tick + 1))
                num_fresh_fruit -= 1
            if col > 0 and (row, col - 1) not in visited and grid[row][col - 1] != 0:
                visited.add((row, col - 1))
                q.append((row, col - 1, tick + 1))
                num_fresh_fruit -= 1

        # Return result
        if num_fresh_fruit == 0:
            if q:   
                tick = q[-1][2]
            return tick
        else:
            return -1

        
