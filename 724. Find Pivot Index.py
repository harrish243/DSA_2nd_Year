class solution:
  def pivotIndex(self , nums : list[int]) -> int:
    total = sum(nums)
    left = 0

    for i in range(len(nums)):
      right = total - left - nums[i]

      if right == left :
        return i

      left = left + nums[i]

    return -1
