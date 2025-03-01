# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        product = 1
        for num in nums:
            answer.append(product)
            product *= num
        product = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = answer[i] * product
            product *= nums[i]
        return answer

solution = Solution()
print(solution.productExceptSelf(nums = [1,2,3,4]))