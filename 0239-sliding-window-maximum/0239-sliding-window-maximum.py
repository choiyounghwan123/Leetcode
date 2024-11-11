# 239. Sliding Window Maximum

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        queue = deque()

        for idx,num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)
            if idx >= k and nums[idx - k] == queue[0] :
                queue.popleft()
            if idx+1 >=k:
                result.append(queue[0])



        return result


print(Solution().maxSlidingWindow(nums = [7,2,4], k = 2))