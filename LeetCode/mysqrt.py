class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2000000000
        mid = (left+right) // 2
        while(True):
            temp = mid
            if x < mid * mid:
                right = mid
            else:
                left = mid
            mid = (left + right) // 2
            if temp == mid:
                break
        return left