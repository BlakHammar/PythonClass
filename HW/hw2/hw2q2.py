'''
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
'''

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