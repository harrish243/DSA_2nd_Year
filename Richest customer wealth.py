class Solution(object):
    def maximumWealth(self, accounts):
        maximum =0
        for i in accounts:
            wealth = sum(i)
            maximum = max(maximum,wealth)
        return maximum
        