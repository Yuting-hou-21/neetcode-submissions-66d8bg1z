class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        res = [0] * length

        curr = 1
        for i in range(length):
            prefix[i] = curr
            curr *= nums[i]

        curr = 1
        for i in range(length - 1, -1, -1):
            suffix[i] = curr
            curr *= nums[i]

        for i in range(length):
            res[i] = prefix[i] * suffix[i]

        return res


