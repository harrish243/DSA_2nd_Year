class Solution:
    def shuffle(self, nums, n):
        return [v for i in range(n) for v in (nums[i], nums[i+n])]
