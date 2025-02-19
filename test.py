# quiz on wednesday datatype 90p (47-115)
#functions(1-27)

def charCount(string):
    charDict = {}
    for char in string:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    
    sortedDict = sorted(charDict.items(), key=lambda x: x[1], reverse=True)

    print(sortedDict)
    return sortedDict[1][1]


string = input("Enter a string: ")

print(charCount(string))