'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 

ans[i] is the number of 1's in the binary representation of i.

'''

n = int(input("Enter a number: "))

ans = [0] * (n+1)

for i in range(n+1):
    ans[i] = bin(i).count("1")

print(ans)