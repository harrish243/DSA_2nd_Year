class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            sumLeft=sum(nums[:i])
            sumRight=sum(nums[i+1:])
            if sumLeft==sumRight:
                return i
        return -1
#724.Find pivot index
#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.