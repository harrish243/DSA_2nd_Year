class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximumWealth = 0

        for account in accounts:
            wealth = sum(account)
            maximumWealth = max(maximumWealth,wealth)

        return maximumWealth