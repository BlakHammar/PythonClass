'''
1.
State the use cases where we can (or it is efficient to) 
use one not the other, and vice versa. Explain why.

Lists and tuples:
        List can be use when you want to be able to change 
        the size of an dataset.

        Tuple can be use when you dont want the data in 
        the dataset to ever change
            Better performance and mem efficent
Lists and sets:
        List can be use when you need an ordered datatype, 
        able to interact through

        Sets can be used to remove duplicate data.
        need to perform ops like union and intersection

Lists and arrays
        List can be used when you need multiple datatypes.

        Arrays can be used to increase code performance 
        and memory efficiency
        or working with large amount of data
'''

'''
2

You have a file 'test.txt' where there is only one line “This 
is a test file”.  Open the file in a read mode and read the line 
and write the line in another file called “new.txt”.
'''

with open("test.txt", "r") as fp:
    line = fp.readline()
    with open("new.txt", "w") as fp2:
        fp2.write(line)

'''
Problem: 3

You are given a text file poetry.txt that has few poetries in it. 

Write a python program to print the number of characters present 

in each line of the given file to a separate text file called data.txt. 

For example, if a line has the string “ The zen of python   “ with few 

white spaces at both ends, you ignore the white spaces at the ends and 

count the characters. The character count of it is 17. P.S. If you have

opened a file, securely close it too.

'''

with open("poetry.txt", "r") as fp:
    lines = fp.readlines()
    with open("data.txt", "w") as fp2:
        for line in lines:
            fp2.write(str(len(line.strip())) + "\n")


'''
Problem: 4

You are given a list of authors and a set of publishing years:

authors = ['Noether', 'Turing', 'Knuth']

years = (1882, 1912, 1938)

Combine these data to create a dictionary called books where 
authors will be the keys and years will be the values.

'''

authors = ['Noether', 'Turing', 'Knuth']
years = (1882, 1912, 1938)

books = dict(zip(authors, years))

'''
Problem: 5

Write a function that counts the occurrence of each character in a 
given string and returns the count of the 2nd most frequently occurring 
character. For example, if the input is 'coffee cuffee' the output will be 
2 corresponding to the letter 'c'. P.S. Do not use the builtin Counter() method.

'''

def charCount(string):
    charDict = {}
    for char in string:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    
    sortedDict = sorted(charDict.items(), key=lambda x: x[1], reverse=True)
    return sortedDict[1][1]


'''
Problem: 6

Write a python code to transpose the following matrix (using zip()):

mat = [[1,2,3], [4,5,6], [7,8,9]] 

'''

mat = [[1,2,3], [4,5,6], [7,8,9]]

print(list(zip(*mat)))


'''

Problem: 7

 State true or false. If true, explain why, and if false, provide a counter example.

Function arguments are passed by value: false, because list can be changed
Function arguments are passed by reference: false, because 
Function arguments are passed by assignment: true, it changes based how you use it

'''


'''

Problem: 8

Carefully read the following code and write the output of the following programs.

# program 

def greet(name):

    print(f"Hello, {name}!")

 

def greet(name, time_of_day=""):

    if time_of_day:

        print(f"Good {time_of_day}, {name}!")

    else:

        print(f"Hello, {name}!")

 

if __name__ == "__main__":

    greet("Alice")               

    greet("Charlie", "afternoon") 

    greet()

'''
'''
Hello, Alice!
Good afternoon, Charlie!
Hello, Charlie!
'''

'''
Problem: 9

Given two strings s and t, return true if the two strings 
are anagrams of each other, otherwise return false. An anagram 
is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

'''

def isAnagram(s, t):
    return sorted(s) == sorted(t)


'''

Problem: 10

Consider the following Python function for temperature conversion:

def temp_convert(temp, from_scale='C', to_scale='F'):

    scales = {'C': lambda t: t, 'F': lambda t: (t - 32) * 5/9, 'K': lambda t: t - 273.15}

    celsius = scales[from_scale](temp)

    

    if to_scale == 'C':

        return celsius

    elif to_scale == 'F':

        return celsius * 9/5 + 32

    elif to_scale == 'K':

        return celsius + 273.15

 
'''


'''
Which of the following function calls will raise a TypeError? Explain why.

A) temp_convert(100, 'C', 'K')
B) temp_convert(temp=100, to_scale='K')
C) temp_convert(100, from_scale='C', to_scale='K')
D) temp_convert(100, 'C', from_scale='F')
'''

'''
D
'''