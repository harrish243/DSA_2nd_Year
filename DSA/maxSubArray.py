class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        
        return max_sum


'''53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.'''