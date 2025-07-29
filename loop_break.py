# break
num = int(input("enter a num : "))

for i in range (1, num+1):
    if i == 6:
        break
    # print(i)

# continue
for i in range (1, num+1):
    if i == 6:
        continue
    print(i)