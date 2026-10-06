gain = [-5, 1, 5, 0, -7]

altitude=[0]
total=0
highest=0

for num in gain:
    total+=num
    altitude.append(total)


for num in altitude:
    if num>highest:
        highest=num

print(highest)