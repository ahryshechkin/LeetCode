from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDist = 0
        lastOne = -1

        for i in range(len(seats)):
            if seats[i] == 1:
                if lastOne == -1:
                    maxDist = i
                else:
                    maxDist = max(maxDist, (i - lastOne) // 2)
                lastOne = i

        return max(maxDist, len(seats) - 1 - lastOne)