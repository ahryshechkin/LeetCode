from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        start = 1
        for i in range(len(nums)):
            prefix[i] = start
            start *= nums[i]

        start = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = start
            start *= nums[i]

        return [prefix[i] * suffix[i] for i in range(len(nums))]
