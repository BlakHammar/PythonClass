#count the frequency of each element in alist.
alist = [1, 32, 5, 78, 9, 9, 9, 9, 1, 1, 1]

adict = {}

for n in alist:
    adict[n] = adict.get(n, 0)+1

print(adict)

