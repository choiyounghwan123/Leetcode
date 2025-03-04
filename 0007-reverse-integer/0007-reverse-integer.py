# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        x.reverse()
        x = "".join(x)
        if x[-1] == "-":
            x = -(int(x[:-1]))
        else:
            x = int(x)
        if -2147483648 >= x or x >= 2147483648:
            return 0
        else:
            return x
solution = Solution()
print(solution.reverse(x = 1534236469))