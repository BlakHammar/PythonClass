arr = []

for x in range(100,200):
        if( x % 3==0 and x %7==0):
              arr.append("FooBar") 
        elif(x%3==0):
            arr.append("Foo")
        elif(x%7==0):
              arr.append("Bar")
        else:
              arr.append(x)

print(arr)


from math import log #math is python library with more adv math

for x in range(2,1000):
      y=x
      for count in range(y):
            x = x // 2
            if x == 0:
                  break

      #print(f"The approx log_2 of y = count -1)
      abs_err =abs(floor(log(y,2)) - count) #abs = absolute value

      #if condition is false, it triggers error message
      assert abs_err < 0.01, "Log calc error"


assert 4 in [2,4,6,8] #returns true since 4 is in list
