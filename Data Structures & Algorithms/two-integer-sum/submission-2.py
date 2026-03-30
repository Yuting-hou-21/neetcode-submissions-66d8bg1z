class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            num = nums[i]

            if num in seen:
                return [seen[num], i]

            seen[dif] = i