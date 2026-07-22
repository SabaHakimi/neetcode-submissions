class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    self.findLand(i, j, grid, num_rows, num_cols)
                    count += 1
        return count

    def findLand(self, i, j, grid, num_rows, num_cols):
        if i >= 0 and i < num_rows and j >= 0 and j < num_cols:
            if grid[i][j] == "1":
                grid[i][j] = "X"
                self.findLand(i - 1, j, grid, num_rows, num_cols) # above
                self.findLand(i, j - 1, grid, num_rows, num_cols) # left
                self.findLand(i + 1, j, grid, num_rows, num_cols) # below
                self.findLand(i, j + 1, grid, num_rows, num_cols) # right






        # - identify all 'island blocks'/'1's
        # - for each unexplored island block, traverse until island fully explored
        #     for each cardinal neighbor:
        #         - mark 'explored'
        #         - traverse all cardinal neighbors
        # - return count


        # pseudocode:
        
        # traverse entire graph, each time a unmarked 1 is reached:
        #     call recursive function:
        #         if in bounds:
        #             mark self
        #             call all neighbors
        #     add 1 to count 


        # note: watch out for out of bounds errors