class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        i, j = len(g)-1, len(s)-1
        g, s = sorted(g), sorted(s)
        
        while min(i, j) >= 0:
            if s[j] >= g[i]:
                count += 1
                j -= 1
            i -= 1
        return count
