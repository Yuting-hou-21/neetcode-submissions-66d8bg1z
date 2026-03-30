class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        best = 1000

        countT = {}
        countS = {}

        for n in t:
            countT[n] = 1 + countT.get(n, 0)

        have, need = 0, len(countT)

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < best:
                    best = r - l + 1
                    res = "" + s[l : r + 1]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res

            
