# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            if n in visited:
                return False
            else:
                visited.add(n)
                temp = 0
                for num in list(str(n)):
                    temp += int(num) ** 2
                if temp == 1:
                    return True
                n = temp

solution = Solution()
print(solution.isHappy(n = 19))