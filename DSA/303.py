class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0

        for i in range(left, right + 1):
            total = total + self.nums[i]

        return total
#303.Range sum query 
#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right