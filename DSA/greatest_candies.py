class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies =max(candies)
        result = []
        for candie in candies:
            if candie + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result        
candies=[2,3,5,1,3]
extraCandies=3
print(Solution().kidsWithCandies(candies,extraCandies))