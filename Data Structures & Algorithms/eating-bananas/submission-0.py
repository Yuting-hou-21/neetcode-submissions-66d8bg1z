class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxB = max(piles)
        l, r = 1, maxB
        res = 0
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / m)
                if hours > h:
                    break
            
            if hours > h:
                l = m + 1
            else:
                r = m - 1
                res = m

        return res