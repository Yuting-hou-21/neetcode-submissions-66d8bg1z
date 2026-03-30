class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            dif = target - num # dif : the number needed by current num

            if dif in seen:
                return [seen[dif], i] # return index

            seen[num] = i

            