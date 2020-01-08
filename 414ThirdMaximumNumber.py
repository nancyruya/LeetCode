class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numss = sorted(list(set(nums)))
        
        if len(numss)<3:
            return max(numss)
        else:
            return numss[-3]
