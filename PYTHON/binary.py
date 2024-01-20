n=int(input())
a=bin(n)[2:]
b=list(a)
b.reverse
h=[]
num=len(b)
count=0
for x in b:
    c=int(x)
    if c==1:
        count+=1
    else:
        continue
h.append(count)
for x in b:
   d=int(x)
   if(d==1):
        e=b.index(x)
        h.append(e)
        break
num-=1
while(num>=0):
     f=int(b[num])
     if(f==1):
        g=num
        h.append(g)
        break
     num-=1
print(*h,sep='#')