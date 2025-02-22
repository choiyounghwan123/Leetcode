# 1051. Height Checker

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        answer = 0
        index = 0
        a = heights.copy()
        for i in range(len(heights)):
            temp = 0
            flag = False
            for j in range(1,len(heights) - i):
                if heights[temp] > heights[j]:
                    heights[temp],heights[j] = heights[j],heights[temp]
                temp += 1

        for i in range(len(heights)):
            if a[i] != heights[i]:
                answer += 1

        return answer


solution = Solution()
print(solution.heightChecker(heights = [1,1,4,2,1,3]))