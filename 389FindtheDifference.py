class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
                s_dict[x] = 1
                
        for y in t:
            if y not in s_dict:
                return y
            elif s_dict[y] == 0:
                return y
            else:
                s_dict[y] -= 1
