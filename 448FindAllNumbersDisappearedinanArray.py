class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set([i for i in range(1, len(nums)+1)])
        b = set(nums)
        return list(a-b)
