class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums:  
            result.append(i)
        for i in nums:
            result.append(i)
        return result    

#another way to do it is to use the extend method of list

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums 