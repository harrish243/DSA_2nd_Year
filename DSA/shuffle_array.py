class Solution(object):
    def shuffle(self, nums, n):
        left=0
        right=n
        new=[]
        for i in nums:
            if left<n:
                new.append(nums[left])
                new.append(nums[right])
                left+=1
                right+=1
        return new