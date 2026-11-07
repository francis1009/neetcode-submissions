class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = 0
        for i in range(len(nums)-1):
            if energy < nums[i]:
                energy = nums[i]
            energy -= 1
            if energy < 0:
                return False
        return True