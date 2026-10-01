class Solution:
    def runningSum(self, nums) -> list[int]:
        runningSum = []

        for i in range(len(nums)):
            if i == 0:
                runningSum.append(nums[i])
            else:
                runningSum.append(runningSum[i - 1] + nums[i])
        
        return runningSum

nums=[1,4,5,6,7]
solution = Solution()
runningSum = solution.runningSum(nums)
print (runningSum)

