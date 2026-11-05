class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in sum_dict:
                sum_dict[nums[i]] = i
            else:
                return [sum_dict[target - nums[i]], i]