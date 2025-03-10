# 424. Longest Repeating Character Replacement

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        left = right = 0

        for right in range(1,len(s)+1):
            counter[s[right-1]]+=1
            max_char_n = counter.most_common(1)[0][1]
            if right - left - max_char_n > k:
                counter[s[left]] -= 1
                left += 1

        return right - left

