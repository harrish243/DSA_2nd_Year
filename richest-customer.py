class Solution(object):
    def maximumWealth(self, accounts):
        maxi = 0
        for i in accounts:
            current = sum(i)
            if maxi <= current:
                maxi = current

        return maxi