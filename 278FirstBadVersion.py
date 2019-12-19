class Solution:
    def firstBadVersion(self, n):
        left = 0
        right = n
        mid = 0
        
        while left < right:
            mid = int((left + right)/2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
