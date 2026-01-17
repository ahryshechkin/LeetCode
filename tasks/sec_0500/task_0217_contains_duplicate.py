from typing import List


class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
