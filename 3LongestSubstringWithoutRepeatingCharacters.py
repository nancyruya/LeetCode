class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        max = 0
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] > start:
                start = dic[s[i]]
                dic[s[i]] = i
            else:
                dic[s[i]] = i
                if i - start > max:
                    max = i - start
                
        return max
