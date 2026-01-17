from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for line in strs:
            key = ''.join(sorted(line))

            groups[key] = groups.get(key, [])
            groups[key].append(line)

        groups = [sorted(v) for v in groups.values()]

        return sorted(groups, key=len)