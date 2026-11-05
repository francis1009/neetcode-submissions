class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1,1]
        for i in range(1,n):
            ans.append(ans[-1] + ans[-2])
        return ans[-1]