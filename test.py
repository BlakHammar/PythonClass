'''
def fib(n):
    a, b = 0, 1

    print(a**2, end="")
    for i in range(1, n):
        a, b = b , a+b
        print(f", {a**2}", end="")


if __name__ == '__main__':
    x = int(input("Enter the number of terms for the sequence: "))

    fib(x)

'''
'''Problem 1:
Write a program to produce the following output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

Solution:
def prime_number_triangle(n):

    for i in range(1, n+1):
        print("#", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

if __name__=="__main__":
    prime_number_triangle(5)

'''


'''

def is_armstrong(n):
    total = 0
    temp = n
    
    while temp > 0:
        digit = temp%10
        
        total += digit**3
        
        temp //= 10
        
    return n==total

if __name__ == "__main__":
    lower = 1
    while lower:
        lower, upper = int(input("Range begin : ")), int(input("Range end: "))
        if lower:
            armstrong_nums = [n for n in range(lower, upper+1) if is_armstrong(n)]
            print(armstrong_nums)
        else:
            break
'''

'''
def HCF(x, y):
    if y!=0:
        return HCF(y, x%y)
    return x

if __name__ == "__main__":
    x, y = int(input("Enter first number: ")), int(input("Enter second number: "))
    print(HCF(x, y))

'''

'''
def checkPalindrome(s: str):
    
    def isalnumeric(c):
        return (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'))

    l, r = 0, len(s)-1
    while l<=r:
        if not isalnumeric(s[1]):
            l += 1
        if not isalnumeric(s[r]):
            r -= 1

        if s[l] != s[r]:
            return False
        l += 1
        r -= 1      
    return True

if __name__ == "__main__":
    s = "raceaecar"
    print(checkPalindrome(s))
'''

'''
alist = [10, 20, [300, 400, [5000, 6000, 999, 7000], 500], 30, 111, 40]
def checkElement(new,alist):
    for l in alist:
        if isinstance(l, int):
            if l>=100 and l<1000:
                new.append(l)
            else:
                pass
        elif isinstance(l,list):
            checkElement(new,l)
    return new

newlist = checkElement([],alist)
print(newlist)
'''

'''
Given a list, list1 = [12, 4, 67, 96, 7, 8, 94, 33]
a. Write the python code that prints a list where each element is multiplied by 3. You must write the
code using map() and lambda function

list1 = [12, 4, 67, 96, 7, 8, 94, 33]
newlist = list(map(lambda x: x*3, list1))
print(newlist)

'''

'''
Write the python code that prints the multiple of all the elements of the given list. You must write
the code using reduce() and lambda function.

from functools import reduce
new = reduce(lambda x,y: x*y, list1)
print(new)

'''



'''
Write a program to count the total number of alphabetic characters and total number of
numeric characters in a given string input.
Try with inputs such as "Hello123 World! 456"

def countCharacters(s):
    countA, countN = 0,0
    for c in s:
        if c.isalpha():
            countA += 1
        elif c.isnumeric():
            countN += 1
        else:
            pass
    return countA, countN

s = "Hello123 World! 456"

alpha, num = countCharacters(s)

print(f"The count for alphabetic character is {alpha} and the count for numeric character is {num}")

'''

'''
Given a string s1, write a program to return the sum and average of the digits that
appear in the string, ignoring all other characters.
Try with inputs such as s1 = "PYnative29@#8496"

def addNumric(s):
    countN = 0
    sum = 0
    for n in s:
        if c.isnumeric()
            count += 1
            sum += int(n)
    avg = sum / count

    return sum, avg

s1 = "PYnative29@#8496"
total, average = findSumAvg(s1)
print(f"The total is {total} and average is {average:.3f}")

'''

'''
Given two strings needle and haystack, return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we
return 0.

def findNeedle(needle, haystack):
    idx = haystack.find(needle)
    return idx

haystack, needle = "sadbutsad", "sad"
print(findeNeedle(needle, haystack))


'''

'''
def rmDup(array):
    temp = array[0]
    newArray = []
    newArray.append(temp)
    
    for x in range(1,len(array)):
        
        if(temp == array[x]):
            pass
        else:
            temp = array[x]
            newArray.append(temp)
            
    
    return len(newArray), newArray

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

lengthOfArr, newNums = rmDup(nums)

print(lengthOfArr, " nums= ", newNums)

'''
'''
Write a program to add item 7000 after 6000 in the following Python List
Given: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


def findItem(list1):
    for item in list1:
        if item==6000:
            ind = list1.index(item)
            list1.insert(ind+1, 7000)
            return
        elif isinstance(item, list):
            findItem(item)
    return list1

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(findItem(list1))

'''

'''
You are given two sorted integer arrays, array1 and array2, of sizes m and n
respectively. Your task is to merge these two arrays into a single sorted array.
Input: array1 = [1, 3, 5, 7, 9], m=5
array2 = [2, 4, 6, 8, 10,11], n=6
Output: Merged array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

'''

'''
def mergeArray(array1, array2):
    merged = array1 + array2
    merged.sort()
    return merged

array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10,11]

print(mergeArray(array1, array2))

'''
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
Input: n = 5
Output: [0,1,1,2,1,2]


def countBits(n):
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = res[i>>1] + (i&1) # i&1 gives you the last digit
    return res

n = 5
print(countBits(n))


'''


'''
Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8



def findMissingNumber(nums):
    n = len(nums)
    sumNums = sum(nums)
    total = (n*(n+1)) //2

    return total - sumNums

nums = [9,6,4,2,3,5,7,0,1]
total = findMissingNumber(nums)
print(f"The number missing in the array/list is {total}")


'''
'''
String Manipulation Challenge: Password Validator
Create a Python program that validates a password based on specific criteria.
The password must meet the following criteria:
1. At least 8 characters long
2. Contains at least one uppercase letter
3. Contains at least one lowercase letter
4. Contains at least one digit
5. Contains at least one special character from @#$%^&*!
6. Does not contain spaces


def pwCheck(s):
    if(len(s) < 8)
        print("Not 8 chars long")
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False
    specialChar = "@#$%^&*!"

        for i in s:
            if i.isupper():
                hasUpper = True
            elif i.islower():
                hasLower = True
            elif i.isdigit():
                hasDigit = True
            elif i in specialChar:
                hasSpecial = True
            elif i.isspace()
                return False
    return hasUpper and hasLower and hasDigit and hasSpecial

def main():
    while True:
        password = input("Enter a password: ")
        if pwCheck(password):
            print("Password is valid!")
            break
        else:
            print("Password is invalid. Please try again.")
            print("Password must:")
            print("- Be at least 8 characters long")
            print("- Contain at least one uppercase letter")
            print("- Contain at least one lowercase letter")
            print("- Contain at least one digit")
            print("- Contain at least one special character from @#$%^&*!")
            print("- Not contain spaces")

if __name__ == "__main__":
    main()
            
'''
'''
def isAnagram(s, t):
    return sorted(s) == sorted(t)

s = "racecar"
t = "carrace"

print(isAnagram(s,t))

s = "jar"
t = "jam"

print(isAnagram(s,t))

'''

'''
You are given a text file called "quotes.txt" that contains several famous quotes. Write a Python program
to count the number of words in each line of the given file and write the results to a new text file called
"word_count.txt". For example, if a line contains the quote "Be the change you wish to see in the world.",
your program should count it as 9 words. Ignore any leading or trailing whitespace in each line.
Additionally, ensure that you open and close the files securely.

def count_words(line):
    return len(line.strip().split())


with open("quotes.txt", "r") as input_file, open("word_count.txt", "w") as output_file:
    for line in input_file:
        word_count = count_words(line)
        output_file.write(f"{word_count}\n")

print("Word counts have been written to word_count.txt")
'''

