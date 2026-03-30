class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        lastIndex = length - 1
        firstIndex = 0
        while firstIndex < lastIndex:
            if not s[firstIndex].isalnum():
                firstIndex += 1
            elif not s[lastIndex].isalnum():
                lastIndex -= 1
            else:
                if s[firstIndex].lower() != s[lastIndex].lower():
                    return False
                firstIndex += 1
                lastIndex -= 1
        return True