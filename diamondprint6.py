n=int(input())
for i in range (0,n+1):
    print(" "*(n-1-i),end=" ")
    print(" *"*(i+1))
for i in range (n):
    print(" "*(i+1-1),end=" ")
    print(" *"*(n+1-i))