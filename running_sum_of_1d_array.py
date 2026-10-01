class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        total=0

        for num in nums:
            total+=num
            output.append(total)

        return output

