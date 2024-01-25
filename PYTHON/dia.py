n=int(input("Enter the number:"))
ch=input("Enter the character:")
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(n-1,n+i):
        print(ch,end="")
    for j in range((n-i)-1,n-1):
        print(ch,end="")
    print()
for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n*2-i-1):
        print(ch,end="")
    print()