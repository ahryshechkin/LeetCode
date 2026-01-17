from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        prefixCount = {0: 1}
        prefixSum = 0

        for num in nums:
            if num % 2 == 1:
                prefixSum += 1
            result += prefixCount.get(prefixSum - k, 0)
            prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1

        return result
