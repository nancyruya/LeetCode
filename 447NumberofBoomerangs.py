class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        
        for x1, y1 in points:
            dicts = {}
            
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                    
                dx = x1-x2
                dy = y1-y2
                d = dx*dx + dy*dy
            
                if d in dicts:
                    result += dicts[d]
                    dicts[d] += 1
                else:
                    dicts[d] = 1
        return result * 2
