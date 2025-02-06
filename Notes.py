'''
Cool string operators:

str.split()

Example 1:
Write a function to convert a Jabber Id (xmpp servers) to an email id:
# Jabbers ids look like shifat@gmail.com/CDEFGB

jID = "shifat@gmail.com/CDEFGB"

print (jID[:jID.find("/")])

splited = jID.split("/")
print(splited[0])

new = [expression for item in oldlist if condition]

# lambda

add= lambda x,y : x+y
print(add(2,3))

# map
s= [11, 22, 13, 5, 776, 8]

new = list(map(lambda x: x**2, s))
print(new)

# filter

new = list(filter(lambda x: x%2==0, s))
print(new)

# reduce
from functools import reduce

new = reduce( lambda x, y: x+y, s)
print(new)

# sorting
s=[('z',55), ('a', 23), ('n', 100)]
s.sort() # will sort by alpha
s.sort(key= lambda x:x[1], reverse=True) #sort by num
print(s)

sort() is implace, memory efficient, only works on list
sorted() returns a new list, works on iterables

newlist = sorted(s, key = lambda x:x[1])
print(newlist)

from collections import deque
nums = [3,1,100]

dq= deque(nums)

dq.appendleft(33)
dq.append(6)

dq.popleft()

dq.rotate(2)

# files

fp = open("test.csv", "w")
for line in fp:
    print(line.split(","))

s= "VZ, 110\nNYSE:GLD, 20\nNYSE:BAC, 100"
fp.write(s)

print(fp.closed) #prints false
fp.close()

withopen("test.csv"", "w") as fp: #automatically closes files 
    print(fp.read()) # not mem efficient, takes full file into memory

    line = fp.readline()
    while line:
        print(line.strip())
        line = fp.readline()
    
    line = fp.readlines() #reads every thin and put into a list, basically same as read

    for l in lines:
        print(l.strip())

    for l in fp.readlines():   #reads one line at a time
        print(l.strip())


# tuples

my_tuple = (1,2,3, ('python', 'code'))
print(my_tuple[3][1])

my_tuple[2] = 100 #doesnt work, imutable

tuple2 = tuple([1,2,3,3])
print(tuple2)


values = (1, 2, 4, 5, 1, 2, 365, 0, 89)
a, *b, c = (1, 2, 4, 5, 1, 2, 365, 0, 89) 
print(a) #1
print(b) #2, 4, 5, 1, 2, 365, 0
print(c) #89


from collections import namedtuple

namedtuple(typename, field_names=)

Student = nametuple("Student", ["fsuID", "name", "major", "gpa"])
s= Student.("ktm22c", "Kobe", "CS", 4.00)

print(s[0]) #print id
print(type(s)) #prints student

#Dictionary ~ hashmap

employee = {
    "name" : "Alice",
    "age" : 25,
    "tasks" : ["backend", "database"]
}

#acess

print(employee["name"])

val = employee.get("phone", "not found")
print(val)
#update
employee["name"] = "John"
employee.update({
    "name" : "jill,
    "age" : 29,
    "tasks" : ["frontend", "UX"],
})
print(employee)

#delete
del employee["age"]

tasks = employee.pop("tasks")

#iterate

for item in employee.keys():
    print(item)

for key, value in employee.items():
    print(key, " : ", value)

print(list(employee.values()))

#remove duplicates with help of dictionary
alist = [1, 32, 5, 78, 9, 9, 9, 9, 1, 1, 1]

dict.fromkeys(alist)

keys = list(dict.fromkeys(alist).keys())
print(keys)



aset{1,2,3,54,6,5,78,96,9}


alist = [12, 1, 2,12, 12, 12, 5,5,5,5,5,5,5,5,9]

print(set(alist))
                    #set get rids of duplicates
alist =(set(alist))


aset = [1,2,3,4,5]
bset = [4,5,6,7,8]

print(aset.intersection(bset))

print(aset.union(bset))

print(aset.difference(bset))

print(aset^bset)

print(aset>bset, aset<bset) #superset, subset

frozenset(aset) # makes a set inmutable


'''