class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        prevlow = prices[0]
        for i in range(len(prices)):
            prevlow = min(prevlow, prices[i])

            if best < prices[i] - prevlow:
                best = prices[i] - prevlow

        return best

            