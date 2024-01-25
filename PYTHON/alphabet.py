a=int(input("Enter the number:"))
b=1
c=[]
for i in range(1,a+1,1):
    d=[]
    for j in range(1,i+1):
        d.append(b)
        print(b,end=" ")
        b+=1
    c.append(d)
    d=[]
    print()
c=c[::-1]
for i in c:
    for j in i:
        print(j,end=" ")
    print()