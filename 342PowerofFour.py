class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        
        if num == 1:
            return True
        else:
            return False
