class Solution:
    def candy(self, ratings: List[int]) -> int:
        result1 = [1]
        for i in range(1,len(ratings)):
            if ratings[i-1] > ratings[i]:
                result1[-1] = max(result1[-1], 2)
                result1.append(1)

            elif ratings[i-1] < ratings[i]:
                result1.append(result1[-1]+1)
            elif ratings[i-1] == ratings[i]:
                result1.append(1)

        for j in range(len(result1), 1, -1):
            if ratings[j - 1] < ratings[j - 2] and result1[j - 1] >= result1[j - 2]:
                result1[j - 2] = result1[j-1] + 1
        return sum(result1)