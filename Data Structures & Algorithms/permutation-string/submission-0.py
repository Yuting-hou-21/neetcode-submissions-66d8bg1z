class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = [0] * 26
        for n in s1:
            check[ord(n) - ord('a')] += 1

        l = 0
        
        checks2 = [0] * 26
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                checks2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            checks2[ord(s2[r]) - ord('a')] += 1
            if checks2 == check:
                return True

        return False
