nums = [2, 5, 1, 3, 4, 7]
n = 3

output = []

left = 0
right = n

while right < len(nums):
    output.append(nums[left])
    output.append(nums[right])

    left += 1
    right += 1

print(output)