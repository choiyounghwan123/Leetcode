# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0

        while left < len(nums)-1 and right < len(nums)-1:
            if nums[left] != 0 and left < len(nums) - 1:
                left += 1
                continue
            elif nums[right] == 0 and right < len(nums)-1:
                right+=1
            print(left,right)
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
            else:
                right+=1

        print(nums)


solution = Solution()
print(solution.moveZeroes(nums = [1,0,0]))