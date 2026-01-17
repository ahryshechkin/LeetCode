from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = [intervals[0]]

        for interval in intervals[1:]:
            last = mergedIntervals[-1]
            if interval[0] <= last[1]:
                mergedIntervals[-1] = [last[0], max(last[1], interval[1])]
            else:
                mergedIntervals.append(interval)

        return mergedIntervals
