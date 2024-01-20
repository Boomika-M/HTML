N=100
n1=0
n2=1
l1=[0,1]
count=0
a=0
while count < N:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       l1.append(nth)
y=int(input("Enter the number to search:"))
for x in l1:
    b=int(x)
    if b == y:
        print("True")
        a+=1
        break
if(a==0):
    print("False")