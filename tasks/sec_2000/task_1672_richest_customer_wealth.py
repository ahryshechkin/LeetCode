from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for account in accounts:
            accountWealth = sum(account)
            maxWealth = max(maxWealth, accountWealth)

        return maxWealth
