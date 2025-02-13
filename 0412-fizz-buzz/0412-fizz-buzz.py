# 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer



"""
    Input: n = 3
    Output: ["1","2","Fizz"]
"""

solution = Solution()
print(solution.fizzBuzz(3))
