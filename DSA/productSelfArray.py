class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1]*n
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans

#238. Product of Array Except Self    
'''The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''