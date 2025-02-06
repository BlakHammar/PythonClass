'''
You are given two sorted integer arrays, array1 and array2, of sizes m and n respectively. Your task is to merge these two arrays into a single sorted array.
'''

arr1 = list(map(int,input("Enter elements separated by space in non-decreasing order: ").split()))
sizeM = int(input("Enter size of array 1: "))


arr2 = list(map(int,input("Enter elements separated by space in non-decreasing order: ").split()))
sizeN = int(input("Enter size of array 2: "))

mergedArr = arr1 + arr2

mergedArr.sort()

print(mergedArr)

