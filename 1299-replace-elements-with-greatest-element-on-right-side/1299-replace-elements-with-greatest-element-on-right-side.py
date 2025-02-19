# 1299. Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        answer = []
        _max = -1
        for i in range(len(arr)-2,-1,-1):
            _max = max(arr[i + 1], _max)
            temp = arr[i]
            arr[i] = _max
            _max = max(temp, _max)
        arr[-1] = -1
        return arr

solution = Solution()
print(solution.replaceElements(arr = [17,18,5,4,6,1]))