''' Intersection of Two Arrays '''
''' https://leetcode.com/problems/intersection-of-two-arrays/description/ '''

class Solution(object):
    def intersection(self, nums1, nums2):
        my_arr = set(nums1).intersection(set(nums2))
        return list(my_arr)