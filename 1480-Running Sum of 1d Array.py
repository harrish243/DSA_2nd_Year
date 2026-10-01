class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        arr = []
        
        for i in nums:
            sum += i
            arr.append(sum)

        return arr 