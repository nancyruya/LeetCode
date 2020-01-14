class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum1 = 0
        for i in range(1, num):
            if num % i == 0:
                sum1 = sum1 + i
        if (sum1 == num):
            return True
        else:
            return False
            
# Time Limit Exceeded
# Last executed input    20996011
