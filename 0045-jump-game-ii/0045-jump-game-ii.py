# 45. Jump Game II

class Solution:
    def jump(self, nums: list[int]) -> int:
        result = 0
        i = 0

        while i < len(nums) - 1:
            print(i)
            if i + nums[i] >= len(nums)-1:
                result+=1
                break
            max_ = 0
            temp = i
            for j in range(1,nums[temp] + 1):
                if temp + j >= len(nums) -1:
                    result+=1
                    return result
                if max_ <= nums[temp + j]:
                    max_ = nums[temp + j]
                    i = temp + j
            result+=1
        return result


solution = Solution()
print(solution.jump(nums = [1,2,1,1,1]))