class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        curr = 1
        for i in range(n):
            res[i] = curr   #result先當prefix
            curr *= nums[i]

        curr = 1
        for i in range(n - 1, -1, -1):
            res[i] *= curr
            curr *= nums[i]

        return res