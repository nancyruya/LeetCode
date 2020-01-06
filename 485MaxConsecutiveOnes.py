class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                result = max(result, count)
                count = 0
        return max(result, count)
