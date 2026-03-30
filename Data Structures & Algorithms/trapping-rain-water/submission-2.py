class Solution:
    def trap(self, height: List[int]) -> int:
        premax = [0] * len(height)
        sufmax = [0] * len(height)

        tmpmax = 0
        for i in range(len(height)):
            if height[i] > tmpmax:
                premax[i] = height[i]
                tmpmax = height[i]
            else:
                premax[i] = tmpmax

        tmpmax = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > tmpmax:
                sufmax[i] = height[i]
                tmpmax = height[i]
            else:
                sufmax[i] = tmpmax

        res = 0
        for i in range(len(height)):
            res += min(premax[i], sufmax[i]) - height[i]

        return res