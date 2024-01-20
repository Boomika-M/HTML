n=input("Enter the number:")
a=len(n)
b=list(n)
i=0
if a==2 or a==4:
    while(i<a):
        temp=b[i]
        b[i]=b[i+1]
        b[i+1]=temp
        i+=2
    c=''.join(map(str,b))
    print(c)
else:
    print("-1")