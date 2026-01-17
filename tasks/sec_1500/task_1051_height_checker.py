from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0

        for i, val in enumerate(sorted(heights)):
            if val != heights[i]:
                cnt += 1

        return cnt
