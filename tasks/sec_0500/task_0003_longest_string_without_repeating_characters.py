class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_position = {}
        left = 0
        size = 0

        for right, ch in enumerate(s):
            if ch in last_position and last_position[ch] >= left:
                left = last_position[ch] + 1

            last_position[ch] = right
            size = max(size, right - left + 1)

        return size
