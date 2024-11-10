# 75. Sort Colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white,blue = 0,0,len(nums) - 1

        while white <= blue:
            print(red,white,blue)
            if nums[white] < 1:
                nums[red],nums[white] = nums[white],nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                nums[blue],nums[white] = nums[white],nums[blue]
                blue -= 1
            else:
                white +=1
        print(nums)


print(Solution().sortColors(nums = [2,0,2,1,1,0]))
