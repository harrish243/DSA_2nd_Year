class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        

        output = []

        left = 0
        right = n

        while right < len(nums):
         output.append(nums[left])
         output.append(nums[right])

         left += 1
         right += 1
    
        return output


