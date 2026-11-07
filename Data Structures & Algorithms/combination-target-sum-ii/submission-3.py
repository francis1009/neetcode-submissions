class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])          # copy
                return
            if remain < 0:
                return
            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])          # make choice
                backtrack(j+1, remain - candidates[j])
                path.pop()                   # undo choice

        backtrack(0, target)
        return res