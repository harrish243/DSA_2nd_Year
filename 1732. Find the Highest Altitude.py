class solution:
  def largestAltitude(self , gain : list[int]) -> int:
    alt = 0
    mx = 0

    for x in gain :
      alt = alt + x
      mx = max(mx , alt)

    return mx
