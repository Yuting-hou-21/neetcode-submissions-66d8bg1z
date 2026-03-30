class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            sortedW = ''.join(sorted(w))
            res[sortedW].append(w)
        return list(res.values())