n=int(input("Enter the number:"))
print("Value of N:",n)
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(j,end='')
    for k in range(2*i-1):
        print(i,end='')
    for j in range(i+1,n+1):
        print(j,end='')
    print()