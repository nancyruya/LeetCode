class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottom = triangle.pop()
        while triangle:
            top = triangle.pop()
            
            for i in range(len(top)):
                top[i] += min(bottom[i], bottom[i+1])
                
            bottom = top
            
        return bottom[0]
