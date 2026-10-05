class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        return [x + extraCandies >= max(candies) for x in candies]
