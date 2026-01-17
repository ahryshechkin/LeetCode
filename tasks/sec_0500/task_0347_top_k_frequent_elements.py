from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        buckets = list()
        for i in range(len(nums) + 1):
            buckets.append([])

        for num, freq in counter.items():
            buckets[freq].append(num)

        result = list()
        for bucket in buckets[::-1]:
            for item in bucket:
                if len(result) < k:
                    result.append(item)

        return result