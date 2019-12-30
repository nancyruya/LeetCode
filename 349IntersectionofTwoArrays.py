class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = set()
        for i in nums1:
            lookup.add(i)
            
        result = []
        for i in nums2:
            if i in lookup:
                result += i,
                lookup.discard(i)
        return result
