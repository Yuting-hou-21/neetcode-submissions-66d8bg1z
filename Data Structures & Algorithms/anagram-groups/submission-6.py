class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for n in strs:
            key = [0] * 26
            for s in n:
                key[ord(s) - ord('a')] += 1
            hashmap[tuple(key)].append(n)

        return list(hashmap.values())