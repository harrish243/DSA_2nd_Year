#maximum subarray-finding total

class Solution(object):
    def maxSubArray(self, nums):
        big = []

        for i in range(len(nums)):
            list = []
            for j in range(i, len(nums)):
                list.append(nums[j])
                tot = sum(list)
                big.append(tot)

        return max(big)


#without time exceeding
class Solution(object):
    def maxSubArray(self, nums):
        tot = nums[0]
        big = nums[0]

        for i in range(1, len(nums)):
            tot = max(nums[i], tot + nums[i])
            big = max(big, tot)

        return big
