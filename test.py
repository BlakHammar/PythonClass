arr = []

for x in range(100,200):
        if( x % 3 == 0 and x % 7 == 0):
              arr.append("FooBar") 
        elif(x % 3 == 0):
            arr.append("Foo")
        elif(x % 7 == 0):
              arr.append("Bar")
        else:
              arr.append(x)

print(arr)