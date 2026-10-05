class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        out = []

        for i in range(0,len(candies)):
            temp = candies[i] + extraCandies
            if(temp >= m):
                out.append(True)
            else:
                out.append(False)
        return out
