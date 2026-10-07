class Solution:
    def pivotIndex(self, nums):
        s=sum(nums); l=0
        for i,x in enumerate(nums):
            if l==s-l-x: return i
            l+=x
        return -1
