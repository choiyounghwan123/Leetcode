# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0, x

        while left <= right:
            mid = (left + right) // 2
            calc = mid * mid

            if calc == x:
                return mid
            elif calc < x:
                left = mid + 1
            else:
                right = mid - 1
        else:

            return right
