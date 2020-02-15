class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        for element in s:
            if element not in t:
                return False
        return True
