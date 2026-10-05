class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = int((len(nums)/2))
        out = []
        for i in range(mid):
            out.append(nums[i])
            out.append(nums[mid + i])
        return out