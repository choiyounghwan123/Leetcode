# 167. Two Sum II - Input array is sorted


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result = []

        for i in range(len(numbers)):
            target_ = target - numbers[i]

            left,right = 0, len(numbers) - 1

            while left <= right:
                mid = (left +right) // 2
                if mid == i:
                    left += 1
                    continue
                if numbers[mid] > target_:
                    right = mid - 1
                elif numbers[mid] < target_:
                    left = mid + 1
                else:
                    return [i+1,mid+1]


# output is [1,2]
print(Solution().twoSum([1,2,3,4,4,9,56,90],target=8))