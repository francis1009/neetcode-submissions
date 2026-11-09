class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        R, C = len(grid), len(grid[0])
        seen = set()
        D = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def bfs(sr,sc):
            q = deque([(sr,sc)])
            seen.add((sr,sc))
            while q:
                (r, c) = q.popleft()
                for dr, dc in D:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and \
                        (nr,nc) not in seen and grid[nr][nc] == "1":
                        seen.add((nr, nc))
                        q.append((nr, nc))
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r,c)
                    res += 1
        return res
