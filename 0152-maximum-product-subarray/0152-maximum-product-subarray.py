# 152. Maximum Product Subarray
"""
Given an integer array nums, find a subarray that has the largest product,
 and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = nums[0]
        minProduct = nums[0]
        maxProduct = nums[0]
        for i in range(1,len(nums)):
            minProduct,maxProduct = min(nums[i] * minProduct, nums[i] * maxProduct, nums[i]), max(nums[i] * minProduct, nums[i] * maxProduct, nums[i])
            result = max(maxProduct,result)
            print(result)
            print(minProduct,maxProduct)
        return result


solution = Solution()
print(solution.maxProduct(nums = [2,3,-2,4]))