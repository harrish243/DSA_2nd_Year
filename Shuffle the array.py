class Solution(object):
    def shuffle(self, nums, n):
        return[x for i in range(n) for x in (nums[i], nums[i+n])]
        