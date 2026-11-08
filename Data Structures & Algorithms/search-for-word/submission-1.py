class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        D = [(1,0), (-1,0), (0,1), (0,-1)]

        def bt(r, c, k):
            if len(word) == k:
                return True
            if not (0 <= r < R and 0 <= c < C):
                return False
            if word[k] != board[r][c]:
                return False
            
            saved = board[r][c]
            board[r][c] = "#"
            for dr, dc in D:
                if bt(r+dr, c+dc, k+1):
                    board[r][c] = saved
                    return True
            board[r][c] = saved
            return False

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and bt(r, c, 0):
                    return True
        return False
        