class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            a = sum(map(int, str(nums[i])))

            if a == i:
                return i

        return -1  