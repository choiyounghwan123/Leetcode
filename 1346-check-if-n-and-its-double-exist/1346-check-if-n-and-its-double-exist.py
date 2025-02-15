# 1346. Check if N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        hash_map = dict()

        for i in range(len(arr)):
            if arr[i] * 2 in hash_map and hash_map[arr[i] * 2] == 0:
                print(arr[i])
                print("1")
                return True
            elif arr[i] in hash_map and hash_map[arr[i]] == 1:
                return True
            hash_map[arr[i]] = 0
            hash_map[arr[i] * 2] = 1
        return False


solution = Solution()
print(solution.checkIfExist(arr = [4,-7,11,4,18]))