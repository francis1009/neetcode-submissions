class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, openP, closeP):
            if len(path) == n*2:
                res.append(path)          # copy
                return
            if openP < n:
                backtrack(path + "(", openP+1, closeP)
            if closeP < openP:
                backtrack(path + ")", openP, closeP+1)

        backtrack("", 0, 0)
        return res