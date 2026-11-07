class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])          # copy
                return
            if remain < 0:
                return
            for j in range(start, len(nums)):
                path.append(nums[j])          # make choice
                backtrack(j, remain - nums[j])
                path.pop()                   # undo choice

        backtrack(0, target)
        return res