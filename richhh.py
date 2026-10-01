class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0

        for customer in accounts:
            wealth = sum(customer)
            maximum = max(maximum, wealth)

        return maximum