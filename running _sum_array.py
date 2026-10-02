'''Running Sum of 1d Array'''
''' https://leetcode.com/problems/running-sum-of-1d-array/ '''

class Solution(object):
    def runningSum(self, nums):
        number = 0
        my_lst = []
        for i in nums:
            number+= i
            my_lst.append(number)

        return my_lst