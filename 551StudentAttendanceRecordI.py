class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        elif s.count('L') > 2 and 'LLL' in s:
            return False
        return True
