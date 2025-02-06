'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
'''

nums = input("Enter elements separated by space in non-decreasing order: ").split()

newNums = set(nums)

print(len(newNums), ", ", sorted(newNums))