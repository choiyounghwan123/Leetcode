# 1089. Duplicate Zeros

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0

        while index != len(arr) - 1:
            if arr[index] == 0:
                index += 1
                arr.insert(index,0)
                arr.pop()
            index += 1
        print(arr)

solution = Solution()
print(solution.duplicateZeros(arr = [1,0,2,3,0,4,5,0]))