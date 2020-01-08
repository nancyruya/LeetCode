class Solution:
    def longestPalindrome(self, s: str) -> int:
        map_dict = dict()

        for i in s:
            if i in map_dict.keys():
                map_dict[i] += 1
            else:
                map_dict[i] = 1
                
        result = 0
        mark = 0
        
        for j in map_dict.keys():
            if map_dict[j]%2 == 1:
                mark = 1
            result += map_dict[j]//2
            
        result = result * 2 + mark
        return result
