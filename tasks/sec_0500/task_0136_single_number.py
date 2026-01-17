from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqueValues = set()

        for num in nums:
            if num in uniqueValues:
                uniqueValues.remove(num)
            else:
                uniqueValues.add(num)

        return uniqueValues.pop()
