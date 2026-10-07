nums = [1,7,3,6,5,6]
leftsum=0
rightsum=0
total=sum(nums)
for i in range(len(nums)):
  
        rightsum=total-leftsum-nums[i]

        if leftsum==rightsum:
              print(i)
              break

        leftsum+=nums[i]