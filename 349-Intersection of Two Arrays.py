class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for num in set(nums1):
            if num in nums2:
                result.append(num)
                
        return result