#739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0]* len(temperatures)
        for i,cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer



print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
