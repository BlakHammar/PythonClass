def isPrime(x):
    if x < 2:
        print("Not Prime")
    for i in range(2, x):
        if x%i == 0:
            print("Not Prime")
            return
    print("Prime")
        

x= int(input("Enter a number: "))

isPrime(x)
