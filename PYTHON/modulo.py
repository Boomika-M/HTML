n=input("Enter the number:")
l1=[]
for num in n:
    a=int(num)
    a=(a+5)%10
    l1.append(a)
if len(l1)==4:
    temp=l1[0]
    l1[0]=l1[2]
    l1[2]=temp
    a=l1[1]
    l1[1]=l1[3]
    l1[3]=a
    
b=''.join(map(str,l1))
print(int(b))
