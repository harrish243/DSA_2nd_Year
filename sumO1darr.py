class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr_sum = 0
        result = []
        for i in nums:
            curr_sum += i
            result.append(curr_sum)
        return result