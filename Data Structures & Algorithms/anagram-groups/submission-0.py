class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for n in strs:
            key = ''.join(sorted(n))
            res[key].append(n)
        return list(res.values())