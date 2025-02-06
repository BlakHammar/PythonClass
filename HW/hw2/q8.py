'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

'''

def missingNumber(nums):
    n = len(nums)
    total = (n * (n + 1)) // 2
    sum_of_nums = sum(nums)
    return total - sum_of_nums

nums = list(map(int,input("Enter elements separated by space: ").split()))

print(missingNumber(nums))

