# 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i = 0
        length = len(arr) - 1

        while i < length and arr[i] < arr[i+1]:
            i += 1
        if i == length or i == 0:
            return False

        while i < length and arr[i] > arr[i+1]:
            i+=1
        if i == length:
            return True
        return False


solution = Solution()
print(solution.validMountainArray(arr = [2,1]))