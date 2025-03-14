# 278. First Bad Version
# The isBadVersion API is already defined for you.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binary_search(1, n)
    def binary_search(self,start,end):
        if start > end:
            return start

        mid = (start + end) // 2

        if isBadVersion(mid):
            return self.binary_search(start,mid-1)
        else:
            return self.binary_search(mid+1,end)
    

