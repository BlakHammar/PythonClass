'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

print("Enter the haystack: ")

haystack = input()

print("Enter the needle: ")

needle = input()

idx = haystack.find(needle)

if idx == -1:
    print("Not found")
else:
    print(idx)

