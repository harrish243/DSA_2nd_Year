'''Kids With the Greatest Number of Candies'''
'''https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/'''
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
       maxi = 0
       for i in range(len(candies)):
        if candies[i]>=maxi:
            maxi = candies[i]
       bool_arr = [candies[i]+extraCandies >= maxi for i in range(len(candies))]
       return bool_arr