from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 2D grid
        # X's and O's
        # 
        # capture surrounded regions (cardinal directions)
        # to capture all surrounded regions, need to find all surrounded regions
        # OR, find all non-surrounded regions, then capture everything else 

        # add all edge O's to queue
        # then discover all neighboring O's
        
        # then 2nd pass iterate entire array and if run into an O not in visited, then mark it X

        q = deque()
        visited = set()

        # get all in first row, first col, last row, last col
        lr = len(board) - 1
        lc = len(board[0]) - 1

        # first row
        for c in range(len(board[0])):
            cell = (0, c)
            if board[0][c] == 'O':
                q.append((0, c))
                visited.add((0, c))

        # last row
        for c in range(len(board[0])):
            cell = (lr, c)
            if cell not in visited and board[lr][c] == 'O':
                q.append(cell)
                visited.add(cell)

        # first col
        for r in range(len(board)):
            cell = (r, 0)
            if cell not in visited and board[r][0] == 'O':
                q.append(cell)
                visited.add(cell) 

        # last col
        for r in range(len(board)):
            cell = (r, lc)
            if cell not in visited and board[r][lc] == 'O':
                q.append(cell)
                visited.add(cell)


        # BFS all queued O's 
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            cell = q.popleft()
            r = cell[0]
            c = cell[1]
            for neighbor in neighbors:
                # calc neighbor idx
                dr = r + neighbor[0]
                dc = c + neighbor[1]
                n = (dr, dc)

                # if neighbor is not in visited and also an 'O', add to q and visited
                if n not in visited:
                    # make sure in bounds too
                    if 0 <= dr < len(board) and 0 <= dc < len(board[0]) and board[dr][dc] == 'O':
                        q.append(n)
                        visited.add(n)

        
        # Iterate array, each time an 'O' is encountered, if not in visited, set to 'X'
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

