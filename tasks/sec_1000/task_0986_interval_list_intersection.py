from typing import List


class Solution:
    def intervalIntersection(self, firstList: list[List[int]], secondList: list[List[int]]) -> list[List[int]]:
        firstPtr, secondPtr = 0, 0
        result = list()

        while firstPtr < len(firstList) and secondPtr < len(secondList):
            firstStart, firstEnd = firstList[firstPtr]
            secondStart, secondEnd = secondList[secondPtr]

            start = max(firstStart, secondStart)
            end = min(firstEnd, secondEnd)
            if start <= end:
                result.append([start, end])

            if firstEnd < secondEnd:
                firstPtr += 1
            else:
                secondPtr += 1

        return result


print((100000 + 30000 - 1) // 30000)