"217. https://leetcode.com/problems/contains-duplicate/"
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = set(nums)
        if len(nums) == len(n):
            return False
        else:
            return True