class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        for can in candies:
            sol = 0
            sol = can + extraCandies
            res.append(sol >= max(candies))        
        return res
