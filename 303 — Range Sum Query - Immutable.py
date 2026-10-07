class NumArray:
    def __init__(self, nums):
        self.p = [0]
        for x in nums:
            self.p.append(self.p[-1] + x)

    def sumRange(self, left, right):
        return self.p[right + 1] - self.p[left]
