class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        mid = len(nums)//2
        left = []
        right = []
        res = []
        for i in range(len(nums)):
            if i < mid:
                left.append(nums[i])
            else:
                right.append(nums[i])
        for i in range(n):
            res.append(left[i])
            res.append(right[i])
        return res

    