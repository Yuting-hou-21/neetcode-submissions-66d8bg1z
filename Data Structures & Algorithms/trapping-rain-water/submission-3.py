class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        res = 0
        preMax = height[i]
        sufMax = height[j]

        while i < j:
            if preMax < sufMax:
                i += 1
                preMax = max(preMax, height[i])
                res += preMax - height[i]
            else:
                j -= 1
                sufMax = max(sufMax, height[j])
                res += sufMax - height[j]

        return res