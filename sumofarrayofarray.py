"1672.https://leetcode.com/problems/richest-customer-wealth/description/"
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum1 = 0 
        maxi = 0
        
        for i in accounts:
            sum1 = sum(i)
            if sum1 > maxi:
                maxi = sum1
        return maxi