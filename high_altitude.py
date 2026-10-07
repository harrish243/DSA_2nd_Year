'''Highest Altitude'''
'''https://leetcode.com/problems/find-the-highest-altitude/'''

class Solution(object):
    def largestAltitude(self, gain):
        start=0
        high=0
        for i in gain:
            start+=i
            high = max(start,high)

        return high