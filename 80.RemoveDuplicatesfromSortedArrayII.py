class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            if result < 2 or n > nums[result-2]:
                nums[result] = n
                result += 1
        return result
