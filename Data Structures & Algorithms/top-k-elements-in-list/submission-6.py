class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        bucketsort = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap.items():
            bucketsort[value].append(key)

        res = []
        for i in range(len(bucketsort) - 1, 0, -1):
            for n in bucketsort[i]:
                res.append(n)
                if len(res) == k:
                    return res