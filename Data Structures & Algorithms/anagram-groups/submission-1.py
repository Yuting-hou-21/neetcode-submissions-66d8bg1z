class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for n in strs:
            freq = [0] * 26
            for i in n:
                freq[ord(i) - ord('a')] += 1
            res[tuple(freq)].append(n)

        return list(res.values())