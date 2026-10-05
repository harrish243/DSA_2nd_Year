class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        Output=[]
        max_candies=max(candies)

        for num in candies:
            if num+extraCandies>=max_candies:
                Output.append(True)
            else:
                Output.append(False)
        return Output
        