from typing import List


class Solution:
    def averageWaitingTime(self, customers: list[List[int]]) -> float:
        currentTime = 0
        totalWaitingTime = 0

        for arrivalTime, orderTime in customers:
            currentTime = max(currentTime, arrivalTime)
            currentTime += orderTime
            totalWaitingTime += currentTime - arrivalTime

        return totalWaitingTime / len(customers)
