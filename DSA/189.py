class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        
        ans = nums[-k:] + nums[:-k]
        
        nums[:] = ans
#189.Rotating Array
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.    