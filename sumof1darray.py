"1480.https://leetcode.com/problems/running-sum-of-1d-array/submissions/2159071506/"
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []
        sum = 0
        for i in nums:
            sum+=i
            li.append(sum)
        return li