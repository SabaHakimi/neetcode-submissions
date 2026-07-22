class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # just use dict

        # rows
        for row in board:
            freqs = set()
            for num in row:
                if num != '.':
                    if num not in freqs:
                        freqs.add(num)
                    else: 
                        return False

        # cols
        for c in range(9):
            freqs = set()
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] not in freqs:
                        freqs.add(board[r][c])
                    else:
                        return False

        # 3x3's
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                freqs = set()
                for rs in range(r, r + 3):
                    for cs in range(c, c + 3):
                       if board[rs][cs] != '.':
                            if board[rs][cs] not in freqs:
                                freqs.add(board[rs][cs])
                            else:
                                return False     

        return True

        # 00 01 02  03 04 05
        # 10 11 12  13 14 15
        # 20 21 22  23 24 25
        #           33 34 35
        #           43 44 45
        #           53 54 55

            
