class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS,dicT = {}, {}

        for i in range(len(s)):
            dicS[s[i]] = 1 + dicS.get(s[i],0)
            dicT[t[i]] = 1 + dicT.get(t[i],0)
        
        return dicS == dicT
