# 1346. Check if N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] * 2 in arr and arr.index(arr[i] * 2) != i:
                return True
        return False


solution = Solution()
print(solution.checkIfExist(arr = [4,-7,11,4,18]))