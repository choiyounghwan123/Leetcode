# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if r* c != len(mat) * len(mat[0]):
            return mat
        answer = []
        r_, c_ = 0, 0
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                temp.append(mat[i][j])
                if len(temp) == c:
                    answer.append(temp)
                    temp = []
            if len(temp) == c:
                answer.append(temp)
                temp = []



        return answer


solution = Solution()
print(solution.matrixReshape(mat=[[1,2,3,4]], r=2, c=2))
