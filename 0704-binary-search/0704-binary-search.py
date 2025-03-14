# 704. Binary Search

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(start,end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start,mid-1)
            else:
                return binary_search(mid+1,end)
        return binary_search(0,len(nums) - 1)

solution = Solution()
print(solution.search(nums = [-1,0,3,5,9,12], target = 9))