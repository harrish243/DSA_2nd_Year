class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        last = nums[-k:]
        first = nums[:-k]
        nums[:] = last + first
        print(nums)

#189.Rotate Array
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

