class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix=[0]
        for num in nums:
            self.prefix.append(self.prefix[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
nums=[-2,0,3,-5,2,-1]
obj=NumArray(nums)
print(obj.sumRange(0,2))