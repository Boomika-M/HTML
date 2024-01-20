n=input("Enter the number:")
a=list(n)
c=[]
for x in a:
    y=int(x)
    if(y<9):
        y+=1
        c.append(y)
    else:
        c.append(y)
b=''.join(map(str,c))
print(b)