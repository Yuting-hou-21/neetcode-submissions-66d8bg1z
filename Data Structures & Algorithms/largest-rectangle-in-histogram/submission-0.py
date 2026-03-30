class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightstack = []
        right = [0] * len(heights)
        rightbound = 0

        for i, height in enumerate(heights):
            if rightstack and height < heights[rightstack[-1]]:
                rightbound = rightstack[-1]

                while rightstack and height < heights[rightstack[-1]]:
                    right[rightstack.pop()] = rightbound

            rightstack.append(i)

        rightbound = rightstack[-1]
        while rightstack:
            right[rightstack.pop()] = rightbound

        leftstack = []
        left = [0] * len(heights)
        leftbound = 0

        for i in range(len(heights) - 1, -1, -1):
            if leftstack and heights[i] < heights[leftstack[-1]]:
                leftbound = leftstack[-1]

                while leftstack and heights[i] < heights[leftstack[-1]]:
                    left[leftstack.pop()] = leftbound

            leftstack.append(i)

        leftbound = leftstack[-1]
        while leftstack:
            left[leftstack.pop()] = leftbound

        res = 0
        for i in range(len(heights)):
            area = (right[i] - left[i] + 1) * heights[i]
            if area > res:
                res = area

        return res


