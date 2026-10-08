class solution:
  def rotate(self , nums : list[int] , k : int) -> None:
    k = k % len(nums)

    if k != o:
      nums[:k] , nums[k:] = nums[-k:] , nums[:-k]
