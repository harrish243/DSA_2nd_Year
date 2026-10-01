class Solution():
    def runningSum(self,nums : list[int]) -> list[int]:
        res = []
        sum = 0
        for i in nums:
            sum += i
            res.append(sum)
        return res

nums = list(map(int, input("Enter the number:").split()))
obj = Solution()
print(obj.runningSum(nums))