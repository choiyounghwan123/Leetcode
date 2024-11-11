class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if target == matrix[row][column]:
                    return True
        return False

print(Solution().searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))