class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        arr = nums + nums
        return arr


        """ n = len(nums)
         ans = [0] * n * 2
         for i in range(n):
             ans[i] = nums[i]
             ans[i+n] = nums[i]

         return ans"""