class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = [None] * len(nums)

        for i in range(len(nums)):
            dif = target - nums[i]
            if nums[i] in seen:
                return [seen.index(nums[i]), i]
            seen[i] = dif
