# 27. Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left,right = 0, len(nums) - 1
        k = len(nums)
        while left <= right:
            if nums[right] == val:
                right -= 1
                k -= 1
                continue
            if nums[left] == val:
                nums[left],nums[right] = nums[right],nums[left]
                k-=1
                right -= 1
            left += 1
        print(nums)
        return k



solution = Solution()
print(solution.removeElement(nums = [2,2,2], val = 2))