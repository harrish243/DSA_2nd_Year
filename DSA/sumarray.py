class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=0
        result =[]
        for num in nums:
            total = total + num
            result.append(total)
        return result
nums=[3,1,2,10,1]
print(Solution().runningSum(nums))