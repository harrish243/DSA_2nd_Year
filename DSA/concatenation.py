class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = []
        result = nums + nums
        return result
nums=[1,2,3]
print(Solution().getConcatenation(nums))