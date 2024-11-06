# 771. Jewels and Stones

import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = collections.Counter(stones)
        result = 0
        for i in jewels:
            if a[i]:
                result += a[i]
        return result

