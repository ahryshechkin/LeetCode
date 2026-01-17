from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join(str(d) for d in digits)) + 1
        return [int(c) for c in str(digit)]
