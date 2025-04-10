# Most Common Word
import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]