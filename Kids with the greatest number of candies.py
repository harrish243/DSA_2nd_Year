class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maximum_candies = max(candies)

        result = []

        for i in candies:
            if i + extraCandies >= maximum_candies:
                result.append(True)
            else:
                result.append(False)

        return result