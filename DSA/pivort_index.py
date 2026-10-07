class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        n =len(nums)
        for i in range (n):
            right = total - left - nums[i]
            if left == right :
                return i
            left += nums[i]
        return -1
nums=[1,7,3,6,5,6]
print(Solution().pivotIndex(nums))
