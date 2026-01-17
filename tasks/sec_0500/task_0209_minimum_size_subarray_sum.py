from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        minLength = len(nums) + 1

        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minLength = min(minLength, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if minLength == len(nums) + 1 else minLength
