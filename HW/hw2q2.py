print("Enter a string: ")

s1 = input()

sum = 0
numOfNums = 0

for i in s1:
    if i.isdigit():
        x = int(i)
        sum += x
        numOfNums += 1

avg =sum / numOfNums

print(sum)
print(avg)