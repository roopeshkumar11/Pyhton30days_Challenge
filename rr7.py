n=int(input())
for i in range (1,n+1):
    if (i==1 or i==n):
      print("1"*n)
    else:
     print("1",end="")   
     print("2"*(n-2),end="") 
     print("1")