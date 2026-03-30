class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        a = []
        for num, freq in count.items():
            a.append([freq, num])
        a.sort()

        res = []
        while len(res) < k:
            res.append(a.pop()[1])
        return res