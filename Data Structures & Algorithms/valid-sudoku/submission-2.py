class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_row = defaultdict(list)
        dict_col = defaultdict(list)
        dict_sqr = defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in dict_row[r] or \
                    board[r][c] in dict_col[c] or \
                    board[r][c] in dict_sqr[(r//3,c//3)]:
                    return False
                dict_row[r].append(board[r][c])
                dict_col[c].append(board[r][c])
                dict_sqr[(r//3,c//3)].append(board[r][c])
                
        return True