class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        greatest = max(candies)

        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result