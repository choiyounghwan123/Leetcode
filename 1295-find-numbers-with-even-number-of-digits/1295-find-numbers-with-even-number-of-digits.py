# 1295. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        answer = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                answer += 1
        return answer

solution = Solution()
print(solution.findNumbers(nums = [12,345,2,6,7896]))