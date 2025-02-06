'''
Write a program to count the total number of alphabetic characters and total number of numeric characters in a given string input.
'''

print("Enter a string: ")

s = input()
totAlpha = 0

totNum = 0

for i in s:
    if i.isalpha() == True:
        totAlpha += 1
    if i.isdigit() == True:
        totNum += 1

print(totAlpha)

print(totNum)