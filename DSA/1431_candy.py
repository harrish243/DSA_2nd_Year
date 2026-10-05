class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for i in candies:
            sum=i+extraCandies
            l=max(candies)
            if sum>=l:
                result.append(True)
            else:
                result.append(False)
        return result