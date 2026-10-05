'''Shuffle the Array'''
'''https://leetcode.com/problems/shuffle-the-array/'''
class Solution(object):
    def shuffle(self, nums, n):
        my_lst = []
        for i in range(n):
            my_lst.append(nums[i])
            my_lst.append(nums[n])
            n+=1
        return my_lst
