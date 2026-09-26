from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # cells connected in cardinal directions
        # regions formed via 'O' cells
        # lets not think of this as 'capturing'
        # need to determine whether a region of O's is surrounded, and if so, convert to 'X's
        # for each O, treat as a starting point for a region
        #   explore via BFS until either:
        #       neighbors/region exhausted
        #       an O in the region is on an edge

        # logistical concerns
        #   need to make sure we don't hit the same region of O's twice and think its different
        #   - visited set
        #   keep track of current region

        # multi-source BFS? no
        
        # Track visited
        visited = set()
        
        # Iterate board and BFS on each unvisited O
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited and board[row][col] == 'O':
                    # Region found, run BFS
                    self.exploreRegion((row, col), board, visited)

    def exploreRegion(self, start, board, visited):
        # Track region and set up BFS queue
        edge_found = False
        region = []
        q = deque()
        q.append((start[0], start[1]))
        region.append((start[0], start[1]))
        visited.add((start[0], start[1]))

        # BFS until region exhausted
        # If edge found, do not convert to X's
        while q:
            # Get current
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

            # Queue neighbors
            for r, c in neighbors:
                # Check in bounds
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
                    # Queue up all neighboring O's
                    if (r, c) not in visited and board[r][c] == 'O':
                        q.append((r, c))
                        region.append((r, c))
                        visited.add((r, c))
                # This node is an edge node if it has out of bounds neighbor
                else:
                    edge_found = True

        # If no edge found, convert O's in region to X's
        if not edge_found:
            for row, col in region:
                board[row][col] = 'X'



