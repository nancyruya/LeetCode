class Solution:
    def longestPalindrome(self, s: str) -> str:
        panlindrome = ''
        
        for i in range(len(s)):
            len1 = len(self.getlongestpanlindrome(s, i, i))
            
            if len1 > len(panlindrome):
                panlindrome = self.getlongestpanlindrome(s, i, i)
                
            len2 = len(self.getlongestpanlindrome(s, i, i+1))
            
            if len2 > len(panlindrome):
                panlindrome = self.getlongestpanlindrome(s, i, i+1)
            
        return panlindrome
            
            
    def getlongestpanlindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
